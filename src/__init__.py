from fastapi import FastAPI 

#create an lifecycle event to connect to db by init an asyncocntextmanager 
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.books.routes import book_router 


@asynccontextmanager
async def lifespan(app: FastAPI):
    #define which event when the server starts 
    # and what to write when the server stops 
    print(f"Server is starting ...")
    # start the db -> async task 
    await init_db()
    yield  
    print(f"Server is shutting down ...")


app = FastAPI(
    title="mind-map",
    version="0.1.0",
    description="A simple example of a FastAPI application",
    # docs_url="/docs",
    # redoc_url="/",
    # openapi_url="/openapi.json"
    lifespan=lifespan
)



## decorator to make a get request to ping endpoint 
# @app.get("/ping")
# async def ping():
#     return {
#         "message":"pong"
#     }

app.include_router(book_router,tags=['books'])