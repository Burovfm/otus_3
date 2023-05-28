import requests
import pytest


@pytest.fixture
def url_and_status(request):
    url = request.config.getoption("--url", default="https://ya.ru")
    status_code = int(request.config.getoption("--status_code", default=200))
    return url, status_code


def test_check_status_code(url_and_status):
    url, expected_status_code = url_and_status
    response = requests.get(url)
    assert response.status_code == expected_status_code
