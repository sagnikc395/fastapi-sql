# define the standard API routes here for the books and the operations permitted

from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel, BookResponseModel
from src.db.main import get_session
from .service import BookService
from http import HTTPStatus

book_router = APIRouter(prefix='/books')

@book_router.get("/",response_model=List[BookResponseModel])
async def read_books(session: AsyncSession = Depends(get_session)):
    '''get all the books'''
    books = await BookService(session).get_all_books()
    return books 

@book_router.post("/",status_code=HTTPStatus.CREATED)
async def create_book(book_create_data:BookCreateModel,
                      session: AsyncSession = Depends(get_session)):
    '''create a new book'''
    book = await BookService(session).create_book(book_create_data)
    return book 

@book_router.get("/{book_id}",status_code=HTTPStatus.OK)
async def read_book(book_id:str, session: AsyncSession = Depends(get_session)):
    '''get a book by its uid'''
    book = await BookService(session).get_book(book_id)
    return book 


@book_router.put("/{book_id}",status_code=HTTPStatus.OK)
async def update_book(
    book_id: str, 
    update_data: BookCreateModel,
    session: AsyncSession = Depends(get_session)
):
    '''update a book '''
    update_book = await BookService(session).update_book(book_id,update_data)
    return update_book

@book_router.delete("/{book_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_book(book_id: str, session: AsyncSession = Depends(get_session)):
    """Delete a book"""
    await BookService(session).delete_book(book_id)
    return {}