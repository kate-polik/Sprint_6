import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from constants import Constants
from config import URLS
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


@pytest.mark.usefixtures("driver")
@allure.feature("Создание заказа")  # Перевод "Order Creation"
class TestOrder:
    @pytest.mark.parametrize(
        "order_button_locator, name, surname, address, metro_locator, phone, date_choice, rental_period_list, color_checkbox, comment",
        [
            (MainPageLocators.ORDER_BUTTON_1, Constants.NAME_1, Constants.SURNAME_1, Constants.ADDRESS_1,
             OrderPageLocators.METRO_FIELD_LIST_1, Constants.PHONE_1, OrderPageLocators.DELIVERY_DATE_CHOICE_1,
             OrderPageLocators.RENTAL_PERIOD_LIST_1, OrderPageLocators.COLOR_CHECKBOX_1, Constants.COMMENT_1),
            (MainPageLocators.ORDER_BUTTON_2, Constants.NAME_2, Constants.SURNAME_2, Constants.ADDRESS_2,
             OrderPageLocators.METRO_FIELD_LIST_2, Constants.PHONE_2, OrderPageLocators.DELIVERY_DATE_CHOICE_2,
             OrderPageLocators.RENTAL_PERIOD_LIST_2, OrderPageLocators.COLOR_CHECKBOX_2, Constants.COMMENT_2),
        ]
    )
    @allure.story("Тестирование создания заказа")  # Перевод "Test Order Creation"
    @allure.title("Создание заказа с параметризованными данными")  # Перевод "Create order with parameterized data"
    def test_create_order(self, driver, order_button_locator, name, surname, address, metro_locator,
                          phone, date_choice, rental_period_list, color_checkbox, comment):
        main_page = MainPage(driver)
        main_page.click_on_cookie()
        order_page = OrderPage(driver)
        order_page.click_on_element(order_button_locator)
        order_page.fill_order_form_part1(name, surname, address, metro_locator, phone)
        order_page.fill_order_form_part2(date_choice, rental_period_list, color_checkbox, comment)
        assert order_page.is_success_modal_visible(), "Окно подтверждения не отображается"

        order_page.click_view_status()
        order_page.click_scooter_logo()
        assert driver.current_url == URLS.URL_MAIN, "Переход на главную страницу 'Самокат' не произошёл"

        order_page.click_yandex_logo()
        order_page.wait_for_url(URLS.URL_DZEN)  # Заменено wait_url
        assert driver.current_url == URLS.URL_DZEN, "Переход на главную страницу Дзена не произошёл"
