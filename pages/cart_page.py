from playwright.sync_api import Page, expect
from Utils.screenshot import Screenshot


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_onesie_in_cart(self):
        # Pastikan produk yang dipilih ada di keranjang
        expect(self.page.get_by_text("Sauce Labs Onesie", exact=True)).to_be_visible(timeout=15000)

        Screenshot.take(
            self.page,
            "produk yang dipilih ada di keranjang",
            timeout=15000
        )

    def proceed_to_checkout(self):
        # Klik tombol Checkout
        self.page.get_by_role("button", name="Checkout").click()

        # Pastikan halaman informasi checkout terbuka
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html", timeout=15000)

        # Cek terdapat text "Checkout: Your Information"
        expect(self.page.locator(".title")).to_have_text("Checkout: Your Information")

        Screenshot.take(
            self.page,
            "Menampilkan halaman Input data diri",
            timeout=15000
        )