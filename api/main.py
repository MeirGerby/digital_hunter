from fastapi import FastAPI
from .routes import router 
from shared import MySQLConnector 

app = FastAPI()
app.include_router(router) 


if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("api.main:app", host="localhost", port=8002, reload=True)