from app.app import app
import uvicorn
import os



if __name__ == "__main__":
    uvicorn.run("main:app", host=os.getenv('HOST_IP'), port=8000, timeout_keep_alive=30, reload=True)