from fastapi import FastAPI 

app = FastAPI()

## decorator to make a get request to ping endpoint 
@app.get("/ping")
async def ping():
    return {
        "message":"pong"
    }
