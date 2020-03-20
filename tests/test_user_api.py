import pytest


async def test_sing_in(client):
    url = "/api/sign_in"
    data = {'username': 'TestUserName1', 'password': 'MyPassword'}
    resp = await client.post(url, json=data)
    assert resp.status == 200


async def test_sing_up(client):
    url = "/api/sign_up"
    data = {'username': 'TestUserName1', 'password': 'MyPassword'}
    resp = await client.post(url, json=data)
    assert resp.status == 200


async def test_redis(app, redis, init_app):
    print('X')
    # print(await redis.get('symbols'))
    print('X')