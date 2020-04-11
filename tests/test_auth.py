import pytest


async def test_sign_in(client):
    url = "/api/sign_in"
    data = {'username': 'TestUserName1', 'password': 'MyPassword'}
    resp = await client.post(url, json=data)
    assert await resp.json() == data
    assert resp.status == 200


async def test_sign_if_fail(client):
    url = "/api/sign_in"
    data = {'username': 'TestUserName1'}
    resp = await client.post(url, json=data)
    # assert resp.status == 200


async def test_sing_up(client, redis):
    url = "/api/sign_up"
    data = {'username': 'TestUserName1', 'password': 'MyPassword'}
    resp = await client.post(url, json=data)
    assert resp.status == 200
    assert await resp.json() == {'data': 'ok'}
