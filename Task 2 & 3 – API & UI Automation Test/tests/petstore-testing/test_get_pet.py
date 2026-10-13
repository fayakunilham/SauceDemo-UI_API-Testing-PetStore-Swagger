from playwright.sync_api import sync_playwright

URL = "https://petstore.swagger.io/v2/pet/findByStatus"
PET_ID = 2026101302


def test_find_pet_by_status():
    with sync_playwright() as p:
        api = p.request.new_context()

        try:
            response = api.get(
                URL,
                params={"status": "available"}
            )

            print("Request URL:", response.url)
            print("GET Status:", response.status)
            print("Response Body:", response.text()[:1000])

            assert response.status == 200, (
                f"Expected 200, got {response.status}: "
                f"{response.text()}"
            )

            pets = response.json()
            assert isinstance(pets, list), (
                "Response harus berupa array JSON"
            )

            found = any(
                str(pet.get("id")) == str(PET_ID)
                and pet.get("name") == "Channa stewartii"
                and pet.get("status") == "available"
                for pet in pets
            )

            assert found, (
                f"Pet dengan ID {PET_ID} tidak ditemukan"
            )

            print("PASS: Pet ditemukan berdasarkan status")

        finally:
            api.dispose()