from playwright.sync_api import Page, expect
from Utils.screenshot import Screenshot


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_customer_information(self):
        # Mengisi informasi customer
        self.page.locator("#first-name").fill("Fayakun")
        self.page.locator("#last-name").fill("Pradana")
        self.page.locator("#postal-code").fill("17100")

        Screenshot.take(
            self.page,
            "Berhasil input informasi customer",
            timeout=15000
        )

        # Klik "Continue" untuk lanjut ke halaman overview
        self.page.get_by_role("button", name="Continue").click()

    def verify_order_overview(self):
        # Memvalidasi halaman ringkasan pesanan
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

        expect(self.page.get_by_text("Sauce Labs Onesie", exact=True)).to_be_visible()

        Screenshot.take(
            self.page,
            "Halaman Checkout",
            timeout=15000
        )

        # Memastikan total pembayaran ditampilkan
        expect(self.page.locator(".summary_total_label")).to_be_visible()

    def finish_checkout(self):
        # Menyelesaikan checkout
        self.page.get_by_role("button", name="Finish").click()

        Screenshot.take(
            self.page,
            "Menyelesaikan checkout",
            timeout=15000
        )

    def verify_checkout_completed(self):
        # Memvalidasi transaksi
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

        # Cek terdapat text ketika sukses transaksi
        expect(self.page.get_by_text("Thank you for your order!", exact=True)).to_be_visible()
        expect(self.page.get_by_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!", exact=True)).to_be_visible()

        Screenshot.take(
            self.page,
            "Transaksi Berhasil",
            timeout=15000
        )