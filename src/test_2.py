import pytest
import requests


@pytest.mark.parametrize("brewery_type", ["micro", "regional", "brewpub", "large", "planning"])
def test_list_breweries_by_type(brewery_type):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_type={brewery_type}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize("state", ["California", "Texas", "Colorado", "New York", "Oregon"])
def test_list_breweries_by_state(state):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_state={state}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_breweries_by_city():
    response = requests.get("https://api.openbrewerydb.org/breweries?by_city=Portland")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize("per_page", [10, 20, 30, 40, 50])
def test_list_breweries_with_pagination(per_page):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?per_page={per_page}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize("query", ["dog", "hop", "ale", "brew", "craft"])
def test_search_breweries_by_name(query):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_name={query}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
