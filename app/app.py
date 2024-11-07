from fastapi import FastAPI, Request, HTTPException
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .routes import routes


app = FastAPI()

  
@app.get('/home')
def home():
    return "hello world!!!"  
    
for route in routes:
    app.include_router(route)
