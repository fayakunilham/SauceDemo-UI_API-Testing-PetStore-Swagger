from playwright.sync_api import Page, expect
from Utils.screenshot import Screenshot


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def add_onesie_to_cart(self):
        # Cari produk berdasarkan nama "Sauce Labs Onesie"
        product = self.page.locator(".inventory_item").filter(has_text="Sauce Labs Onesie")

        # lalu klik tombol "Add to cart" milik produk tersebut
        expect(product).to_be_visible()
        product.get_by_role("button", name="Add to cart").click()

        Screenshot.take(
            self.page,
            "Berhasil memilih produk",
            timeout=15000
        )

    def open_cart(self):
        # Klik ikon keranjang
        self.page.locator(".shopping_cart_link").click()