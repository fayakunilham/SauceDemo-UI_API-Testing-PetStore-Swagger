from asyncio import timeout

from playwright.sync_api import Page, expect
from Utils.screenshot import Screenshot

class LoginPage:

    def __init__(self, page : Page):
        self.page = page

        self.logo = page.locator(".login_logo")
        self.username_input = page.locator('input[data-test="username"]')
        self.password_input = page.locator('input[data-test="password"]')
        self.login_button = page.locator('button[type="submit"], input[type="submit"]')

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

        expect(self.logo).to_have_text("Swag Labs", timeout=15000)
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()

        Screenshot.take(
            self.page,
            "Halaman Login",
            timeout=15000
        )

        expect(self.login_button).to_have_text("Login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)

        Screenshot.take(
            self.page,
            "Input Username dan Password",
            timeout=15000
        )
        self.login_button.click()

    def verify_login_success(self):
        # Memastikan user masuk ke halaman Products
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(self.page.get_by_text("Products", exact=True)).to_be_visible()

        Screenshot.take(
            self.page,
            "Login Success & berhasil menuju halaman Home",
            timeout=15000
        )