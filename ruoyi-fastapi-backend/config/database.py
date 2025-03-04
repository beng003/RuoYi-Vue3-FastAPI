from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from urllib.parse import quote_plus
from config.env import DataBaseConfig

ASYNC_SQLALCHEMY_DATABASE_URL = (
    f'mysql+asyncmy://{DataBaseConfig.db_username}:{quote_plus(DataBaseConfig.db_password)}@'
    f'{DataBaseConfig.db_host}:{DataBaseConfig.db_port}/{DataBaseConfig.db_database}'
)
if DataBaseConfig.db_type == 'postgresql':
    ASYNC_SQLALCHEMY_DATABASE_URL = (
        f'postgresql+asyncpg://{DataBaseConfig.db_username}:{quote_plus(DataBaseConfig.db_password)}@'
        f'{DataBaseConfig.db_host}:{DataBaseConfig.db_port}/{DataBaseConfig.db_database}'
    )

# note: SQLAlchemy的异步引擎和会话生成器
# 创建异步引擎
async_engine = create_async_engine(
    ASYNC_SQLALCHEMY_DATABASE_URL,
    echo=DataBaseConfig.db_echo,
    max_overflow=DataBaseConfig.db_max_overflow,
    pool_size=DataBaseConfig.db_pool_size,
    pool_recycle=DataBaseConfig.db_pool_recycle,
    pool_timeout=DataBaseConfig.db_pool_timeout,
)

# ！！！创建异步会话
AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=async_engine)

# 定义数据模型
class Base(AsyncAttrs, DeclarativeBase):
    pass

# note: SQLAlchemy的异步引擎核心使用场景
# 1. 定义数据模型
# class User(Base):
#     __tablename__ = "users"
    
#     id = mapped_column(Integer, primary_key=True)
#     name = mapped_column(String(50))
#     email = mapped_column(String(100), unique=True)
# 2. 数据库会话使用
# async def create_user(user_data: dict):
#     async with AsyncSessionLocal() as session:
#         async with session.begin():  # 自动事务管理
#             new_user = User(**user_data)
#             session.add(new_user)
#         # 自动提交并关闭会话
#     return new_user
# 3. 表结构初始化
# async def init_db():
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
# 4. 复杂查询示例
# async def get_users_by_age(age: int):
#     async with AsyncSessionLocal() as session:
#         stmt = select(User).where(User.age > age)
#         result = await session.execute(stmt)
#         return result.scalars().all()
