# correct
from fastapi import FastAPI
from urls.router import router as urls_router
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    # await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(urls_router)