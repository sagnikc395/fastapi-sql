from sqlalchemy.ext.asyncio import create_async_engine
from src.config import settings
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel,text
from sqlalchemy.orm import sessionmaker

async_engine = create_async_engine(
    url=settings.POSTGRES_DB,
    echo=True,
)

async def init_db():
    #create the db tables 
    async with async_engine.begin() as conn:
        from .models import Book 
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    '''
    DI to provide the session object 
    '''
    async_session = sessionmaker(
        bind=async_engine,
        class_ = AsyncSession,
        expire_on_commit=False
    )

    async with async_session() as session:
        yield session 

        