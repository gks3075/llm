from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .chatGPT import chatGPT


class Data(BaseModel):
    text: str

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_result(text: str):
    result = chatGPT(text)
    return {"reply": result}

@app.post("/predict")
def get_prediction(data: Data):
    result = chatGPT(data.text)
    return {"reply": result}