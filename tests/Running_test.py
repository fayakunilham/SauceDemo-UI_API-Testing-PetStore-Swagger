import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Pengujian SauceDemo")
class TestSauceDemo:

    @allure.story("Pengujian Login")
    @allure.title("TC-01 - Login berhasil")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success(self, page):
        login = LoginPage(page)

        with allure.step("Membuka website SauceDemo"):
            login.open()

        with allure.step("Login menggunakan akun valid"):
            login.login(
                username="standard_user",
                password="secret_sauce"
            )

        with allure.step("Memastikan login berhasil"):
            login.verify_login_success()

    @allure.story("Pengujian Checkout")
    @allure.title("TC-02 - Checkout Sauce Labs Onesie")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_e2e_checkout_flow(self, page):
        login = LoginPage(page)
        inventory = InventoryPage(page)
        cart = CartPage(page)
        checkout = CheckoutPage(page)

        with allure.step("1. Membuka website dan login"):
            login.open()
            login.login(
                username="standard_user",
                password="secret_sauce"
            )
            login.verify_login_success()

        with allure.step("2. Menambahkan Onesie ke keranjang"):
            inventory.add_onesie_to_cart()

        with allure.step("3. Memverifikasi produk di keranjang"):
            inventory.open_cart()
            cart.verify_onesie_in_cart()

        with allure.step("4. Melanjutkan ke checkout"):
            cart.proceed_to_checkout()

        with allure.step("5. Mengisi informasi pelanggan"):
            checkout.fill_customer_information()

        with allure.step("6. Memverifikasi ringkasan dan harga"):
            checkout.verify_order_overview()

        with allure.step("7. Menyelesaikan checkout"):
            checkout.finish_checkout()

        with allure.step("8. Memastikan checkout berhasil"):
            checkout.verify_checkout_completed()