from sqlalchemy.ext.asyncio import create_async_engine
from src.config import settings
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import text 

async_engine = create_async_engine(
    url=settings.POSTGRES_DB,
    echo=True,
)

async def init_db():
    # setup connection to db and connect to our db 
    async with AsyncSession() as session:
        stmt = text("SELECT 'hello';")
        result = await session.exec(stmt)
        # test db connecton 
        print(result)