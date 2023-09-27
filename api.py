from fastapi import FastAPI, File, UploadFile,BackgroundTasks
from fastapi.responses import JSONResponse
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import csv
import codecs


app = FastAPI()

upload_dir = "uploads"

# Create the directory if it doesn't exist.
os.makedirs(upload_dir, exist_ok=True)

origins = [
    "http://localhost:3000",  # Add your React frontend URL here.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/post")
def post(data: Dict[str, Any]):
    return {"message": "Success"}

@app.post("/upload")
async def upload_csv(file: UploadFile):
    try:
        # Save the uploaded CSV file to the upload directory.
        with open(os.path.join(upload_dir, file.filename), "wb") as f:
            shutil.copyfileobj(file.file, f)
        
        return JSONResponse(content={"message": "File uploaded successfully"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post('/api/upload')
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file).head()
    return df


