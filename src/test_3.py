import pytest
import random
import requests


@pytest.mark.positive
@pytest.mark.parametrize('userId, userId_in_response', [
    (1, 1), (3, 3), (9, 9)
])
def test_api_filtering(base_url, userId, userId_in_response):
    r = requests.get(
        base_url + "/posts",
        params={'userId': userId}
    )
    assert r.status_code == 200
    res_json = r.json()
    random_post_number = random.randint(1, 10)
    assert res_json[random_post_number]['userId'] == userId_in_response
    assert len(res_json) > 0


@pytest.mark.positive
@pytest.mark.parametrize('input_id, output_id', [
    (454, '454'),
    (-3, '-3'),
    (0, '0')
])
@pytest.mark.parametrize('input_title, output_title', [
    ('title', 'title'),
    ('', ''),
    (88, '88')
])
def test_api_post_request(base_url, input_id, output_id, input_title, output_title):
    r = requests.post(
        base_url + "/posts",
        data={'title': input_title, 'body': 'bar', 'userId': input_id})
    assert r.status_code == 201
    res_json = r.json()
    assert res_json['title'] == output_title
    assert res_json['body'] == 'bar'
    assert res_json['userId'] == output_id


@pytest.mark.negative
@pytest.mark.parametrize('userId', [0, -7, 76, 'h'])
def test_api_empty_response(base_url, userId):
    res = requests.get(
        base_url + "/posts",
        params={'userId': userId}
    )
    assert res.status_code == 200
    assert res.json() == []


@pytest.mark.negative
@pytest.mark.parametrize('albumId', [-1, 0, ''])
def test_api_response(base_url, albumId):
    r = requests.get(
        base_url + "/photos",
        params={'albumId': albumId}
    )
    assert r.status_code == 200
    assert r.json() == []


@pytest.mark.negative
@pytest.mark.parametrize("resource", ["users", "posts", "comments"])
def test_get_resource_not_found(base_url, resource):
    response = requests.get(f"{base_url}/{resource}/999")
    assert response.status_code == 404
    assert response.json() == {}


@pytest.mark.positive
def test_create_resource(base_url):
    data = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }
    response = requests.post(f"{base_url}/posts", json=data)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert response.json()["title"] == data["title"]
    assert response.json()["body"] == data["body"]
    assert response.json()["userId"] == data["userId"]
    assert "id" in response.json()
