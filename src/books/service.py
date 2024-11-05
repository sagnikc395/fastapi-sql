from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import Book 
from .schemas import BookCreateModel
from sqlmodel import select


class BookService:
    '''
    class providing methods to create, read,update and delete the books 
    '''

    def __init__(self,session: AsyncSession):
        self.session = session 

    async def get_all_books(self):
        '''
        get a list of all books 
        '''
        stmt = select(Book).order_by(Book.created_at)
        result = await self.session.exec(stmt)
        return result.all()
    
    async def create_book(self,book_create_date: BookCreateModel):
        '''
        creates a new book and returns a instance of the book 
        '''
        book = Book(**book_create_date.model_dump())
        self.session.add(book)
        await self.session.commit()
        return book 
    
    async def get_book(self,book_uid: str):
        '''
        get a book by its UUID.
        '''
        stmt = select(Book).where(Book.uid == book_uid)
        result = await self.session.exec(stmt)
        return result.first()
    
    async def update_book(self,book_uid,book_update_data: BookCreateModel):
        '''
        update a given book
        '''
        stmt = select(Book).where(Book.uid == book_uid)
        result = await self.session.exec(stmt)
        book = result.first()

        for k,v in book_update_data.model_dump().items():
            setattr(book,k,v)

        await self.session.commit()

        return book 
    
    async def delete_book(self,book_uid):
        '''
        delete a book 
        '''
        stmt = select(Book).where(Book.uid == book_uid)
        result = await self.session.exec(stmt)

        book = result.first()

        await self.session.delete(book)
        await self.session.commit()

