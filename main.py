from fastapi import FastAPI
from pydantic import BaseModel
from cryptography.fernet import Fernet
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["https://secure-notes-frontend-alpha.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "p"
cipher = Fernet(gkpzZSjk_ynmBohgT8z-U247l2Hn_i7o7c5KCrTCHt8=)

PASSWORD = "1976"

class TextData(BaseModel):
    text:str

class PasswordData(BaseModel):
    password:str

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is working 🚀"}

@app.post("/login")
def login(data:PasswordData):
    return {"status":"success" if data.password == PASSWORD else "fail"}

@app.post("encrypt")
def encrypt(data:TextData):
    encrypted = cipher.encrypt(data.text.encode())
    return{"encrypted":encrypted.decode()}

@app.post("/decrypt")
def decrypt(data:TextData):
    decrypted = cipher.decrypt(data.text.decode())
    return{"decrypted":decrypted.decode()}
