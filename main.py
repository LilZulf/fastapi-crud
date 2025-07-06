from fastapi import FastAPI, Request, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import json
from pathlib import Path
import shutil

app = FastAPI()
app.mount("/uploads", StaticFiles(directory="context/uploads"), name="uploads")
templates = Jinja2Templates(directory="frontend")
DATA_PATH = Path("context/context.json")
UPLOADS_PATH = Path("context/uploads")
UPLOADS_PATH.mkdir(parents=True, exist_ok=True)

# Init data file
if not DATA_PATH.exists():
    DATA_PATH.write_text(json.dumps([]))

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/receive-json")
async def receive_json(
    name: str = Form(...),
    email: str = Form(...),
    model: str = Form(None),
    file: UploadFile = None
):
    saved_filename = None
    if file and file.filename: 
        saved_filename = UPLOADS_PATH / file.filename
        with saved_filename.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    # Store only metadata in JSON
    new_entry = {
        "name": name,
        "email": email,
        "model": model,
        "file": file.filename if file else None
    }

    existing_data = json.loads(DATA_PATH.read_text())
    existing_data.append(new_entry)
    DATA_PATH.write_text(json.dumps(existing_data, indent=2))

    return {"message": "Data received and stored", "data": new_entry}

@app.get("/data")
async def get_stored_data():
    return json.loads(DATA_PATH.read_text())

@app.put("/update/{index}")
async def update_item(
    index: int,
    name: str = Form(...),
    email: str = Form(...),
    model: str = Form(None),
    file: UploadFile = None
):
    data = json.loads(DATA_PATH.read_text())

    if index < 0 or index >= len(data):
        raise HTTPException(status_code=404, detail="Data not found")

    updated = {
        "name": name,
        "email": email,
        "model": model,
        "file": data[index]["file"]  # Default: keep old file
    }

    # If new file is uploaded
    if file and file.filename:
        saved_filename = UPLOADS_PATH / file.filename
        with saved_filename.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        updated["file"] = file.filename

    # Replace old data
    data[index] = updated
    DATA_PATH.write_text(json.dumps(data, indent=2))

    return {"message": "Data updated", "data": updated}

@app.delete("/delete/{index}")
async def delete_item(index: int):
    data = json.loads(DATA_PATH.read_text())
    if 0 <= index < len(data):
        deleted = data.pop(index)
        DATA_PATH.write_text(json.dumps(data, indent=2))
        return {"message": "Deleted", "data": deleted}
    return JSONResponse(status_code=404, content={"message": "Item not found"})

