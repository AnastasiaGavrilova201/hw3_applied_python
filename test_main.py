from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession
from main import app #, get_async_session
from unittest.mock import AsyncMock

client=TestClient(app=app)

def test_expired_urls():
    response =  client.get("/links/show_expired_url")
    assert response.status_code == 200
    assert response.json()[0].keys() == set(['id', 'url','url_short', 'expires_at', 'created_at'])

def test_shorten():
    response =  client.post("/links/shorten", json={
        "your_url": "https://www.geeksforgeeks.org/testing-fastapi-application/"
    })
    assert response.status_code == 200

def test_short_custom():
    response =  client.post("/links/shorten", json={
        "your_url": "https://www.geeksforgeeks.org/testing-fastapi-application/",
        'custom_alis': 'www'
    })
    assert response.status_code == 200

def test_stats():
    response =  client.get("/links/stats?short_code=https%3A%2F%2Ftinyurl.com%2F29qolf9k")
    assert response.status_code == 200

def test_get_url():
    response =  client.get("/links/?short_code=https%3A%2F%2Ftinyurl.com%2F29qolf9k")
    assert response.status_code == 200

def test_search_url():
    response =  client.get("/links/search?original_url=https%3A%2F%2Fwww.geeksforgeeks.org%2Ftesting-fastapi-application%2F")
    assert response.status_code == 200

def test_update_url():
    response =  client.put("/links/?url=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F74360992%2Fhow-to-cache-data-in-fastapi")
    assert response.status_code == 200
    assert response.json()['message'] == "Updated url: https://stackoverflow.com/questions/74360992/how-to-cache-data-in-fastapi"

def test_delete_url():
    response =  client.delete("/links/?short_code=https%3A%2F%2Ftinyurl.com%2F24he49sj")
    assert response.status_code == 200
    assert response.json()['message'] == "Url https://tinyurl.com/24he49sj deleted"


