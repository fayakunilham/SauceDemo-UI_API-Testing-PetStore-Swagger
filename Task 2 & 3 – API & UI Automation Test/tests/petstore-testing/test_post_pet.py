import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://petstore.swagger.io/v2/pet"

PET_DATA = {
    "id": 2026101302,
    "category": {
        "id": 1,
        "name": "Fish"
    },
    "name": "Channa stewartii",
    "photoUrls": [
        "https://id.pinterest.com/pin/channa-stewarti--755478906258432516/"
    ],
    "tags": [
        {"id": 1, "name": "Channa"},
        {"id": 2, "name": "Freshwater Fish"},
        {"id": 3, "name": "Predatory Fish"}
    ],
    "status": "available"
}


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_add_pet():
    with sync_playwright() as p:
        api = p.request.new_context()

        try:
            response = api.post(
                BASE_URL,
                data=PET_DATA,
                headers={"Content-Type": "application/json"}
            )

            print("Request URL:", response.url)
            print("POST Status:", response.status)
            print("Response Body:", response.text())

            assert response.status == 200, (
                f"Expected 200, got {response.status}: "
                f"{response.text()}"
            )

            data = response.json()

            assert data["id"] == PET_DATA["id"]
            assert data["name"] == PET_DATA["name"]
            assert data["status"] == PET_DATA["status"]

            print("PASS: Pet berhasil ditambahkan")

        finally:
            api.dispose()
