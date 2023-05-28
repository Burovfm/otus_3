import requests
import pytest


def test_all_breeds():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200
    assert len(response.json()["message"]) > 0


breeds = ["affenpinscher", "akita", "beagle", "chow", "dalmatian"]


@pytest.mark.parametrize("breed", breeds)
def test_random_dog_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["message"].startswith("https://")


@pytest.mark.parametrize("breed", ["hound", "terrier", "pinscher", "spaniel", "mastiff"])
def test_all_subbreeds_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/list")
    assert response.status_code == 200
    assert len(response.json()["message"]) > 0


def test_all_breeds_sorted():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200
    breeds = list(response.json()["message"].keys())
    sorted_breeds = sorted(breeds)
    assert breeds == sorted_breeds


@pytest.mark.parametrize("breed", breeds)
def test_all_images_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images")
    assert response.status_code == 200
    assert len(response.json()["message"]) > 0
    for image_url in response.json()["message"]:
        assert image_url.startswith("https://")


@pytest.mark.parametrize("breed", ["bulldog", "retriever", "poodle", "beagle", "boxer"])
def test_random_image_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"].endswith(".jpg")


def test_random_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"].endswith(".jpg")


def test_list_all_breeds():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200
    assert "message" in response.json()
    assert isinstance(response.json()["message"], dict)


@pytest.mark.parametrize("sub_breed", ["boston", "english", "french"])
def test_random_sub_breed_image(sub_breed):
    response = requests.get(f"https://dog.ceo/api/breed/bulldog/{sub_breed}/images/random")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"].endswith(".jpg")


def test_random_image_not_found():
    response = requests.get("https://dog.ceo/api/breed/nonexistent/images/random")
    assert response.status_code == 404
    assert "message" in response.json()
    assert response.json()["message"] == "Breed not found (master breed does not exist)"

