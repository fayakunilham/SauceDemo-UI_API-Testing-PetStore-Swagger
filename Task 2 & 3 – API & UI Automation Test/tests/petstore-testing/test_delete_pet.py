import pytest
from playwright.sync_api import sync_playwright

URL = "https://petstore.swagger.io/v2/pet"
PET_ID = 2026101302


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_delete_pet():
    with sync_playwright() as p:
        api = p.request.new_context()

        try:
            response = api.delete(f"{URL}/{PET_ID}")

            print("Request URL:", response.url)
            print("DELETE Status:", response.status)
            print("Response Body:", response.text())

            assert response.status == 200, (
                f"Expected 200, got {response.status}: "
                f"{response.text()}"
            )

            data = response.json()

            assert str(data.get("message")) == str(PET_ID), (
                "ID pada respons penghapusan tidak sesuai"
            )

            print("PASS: Pet berhasil dihapus")

        finally:
            api.dispose()
