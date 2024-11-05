# define our schema here to create 

from sqlmodel import SQLModel, Field,Column 
import sqlalchemy.dialects.postgresql as pg 
from uuid import UUID,uuid64 
from datetime import datetime 

class Book(SQLModel,table = True):
    '''
    repr the book in a db 
    '''
    __tablename__ = 'books'
    uid: UUID = Field(
        sa_column=Column(pg.UUID,primary_key=True,unique=True, default=uuid64)
    )
    title:str 
    author: str 
    isbn: str 
    description: str 
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))

    def __repr__(self) -> str:
        return f"Book => {self.title}"
    
    