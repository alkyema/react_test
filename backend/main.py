from fastapi import FastAPI, Request, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from typing import List, Optional
import assis

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return "hello it is working"

@app.get("/default")
def default():
    return "hello it is working"

class filterClass(BaseModel):
    user_input: str


@app.post("/response")
def response(filterClass: filterClass, request: Request):
    
    print(filterClass.user_input)
    return assis.choice(filterClass.user_input)
