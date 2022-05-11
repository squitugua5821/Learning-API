import fastapi
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {'Data': 'Team'}

@app.get("/About")
def about():
    return {'Data Man': 'This is all about me'}
