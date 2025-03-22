from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
import time
from datetime import datetime
import pyshorteners
from database import get_async_session
from .models import user
from .schemas import ShortenRequest
from fastapi_cache.decorator import cache
#from fastapi.responses import RedirectResponse
#import starlette.status as status


router = APIRouter(
    prefix="/links",
    tags=["urls"]
)


@router.post("/shorten")
@cache(expire=60)
async def shorten(data: ShortenRequest, session: AsyncSession=Depends(get_async_session)):
    url = data.your_url
    custom_alias = data.custom_alias
    expires_at = data.expires_at
    created_at = datetime.now()
    p = pyshorteners.Shortener()
    short_url = p.tinyurl.short(url)
    if custom_alias is not None:
        query = select(user.c.url).where(user.c.url_short == custom_alias)
        result = await session.execute(query)
        res = result.scalars().all()
        if not res:
            short_url = custom_alias
    my_data = {'url': url, 'url_short': short_url, 'expires_at':expires_at, 'created_at':created_at}
    statement = insert(user).values(my_data)
    await session.execute(statement)
    await session.commit()
    return {'your_url':short_url}

@router.get("/")
async def return_url(short_code: str, session: AsyncSession=Depends(get_async_session)):
    query = select(user.c.url).where(user.c.url_short == short_code)
    result = await session.execute(query)
    res = result.scalars().all()
    if not res:
        return f'Url {short_code} does not exist'
    else:
        return res #RedirectResponse(url=res, status_code=status.HTTP_302_FOUND)

@router.get("/stats")
async def return_stat(short_code: str, session: AsyncSession=Depends(get_async_session)):
    query = select(user.c.url).where(user.c.url_short == short_code)
    result = await session.execute(query)
    url = result.scalars().all()
    query = select(user.c.created_at).where(user.c.url_short == short_code)
    result = await session.execute(query)
    created_at = result.scalars().all()
    if not url:
        return f'Url {short_code} does not exist'
    else:
        return {'created_at': created_at,
                'click_cnt': 1,
                'last_click_dt': datetime.now(),
                'original_url': url}

@router.get("/search")
async def search_url(original_url: str, session: AsyncSession=Depends(get_async_session)):
    query = select(user.c.url_short).where(user.c.url == original_url)
    result = await session.execute(query)
    url = result.scalars().all()
    if not url:
        return f'Url {original_url} does not exist'
    else:
        return {'short_url': url}

@router.delete("/")
@cache(expire=60)
async def delete_url(short_code: str, session: AsyncSession=Depends(get_async_session)):
    query = delete(user).where(user.c.url_short == short_code)
    await session.execute(query)
    await session.commit()
    return {'message': f'Url {short_code} deleted'}

@router.put("/")
@cache(expire=60)
async def update_url(url: str, session: AsyncSession=Depends(get_async_session)):
    p = pyshorteners.Shortener()
    short_url = p.tinyurl.short(url)
    query = update(user).where(user.c.url == url).values(url_short=short_url)
    await session.execute(query)
    await session.commit()
    return {'message': f'Updated url: {url}'}

@router.get("/show_expired_url")
async def show_expired_url(session: AsyncSession=Depends(get_async_session)):
    query = select(user).where(user.c.expires_at < datetime.now())
    result = await session.execute(query)
    url = result.mappings().all()
    if not url:
        return f'Expired urls do not exist'
    else:
        return url