# define the standard API routes here for the books and the operations permitted

from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel, BookResponseModel

book_router = APIRouter(prefix='/books')

@book_router.get("/",response_model=List[BookResponseModel])