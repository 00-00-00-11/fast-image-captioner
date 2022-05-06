from setup import *
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from multiprocessing.pool import ThreadPool

import uvicorn
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
  return "Alive"

@app.post("/predict")
async def predict(request: Request):
  try:
    data = await request.json()
    
    img = await client.aencode([data["url"]])
    caption = random.choice(encoded.find(query=img, limit=10)[0].texts)

    del img
    del data
    
    return caption
  except Exception as e:
    return str(e)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8080)