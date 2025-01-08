from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step('Принять cookie')
    def click_on_cookie(self):
        self.click_on_element(MainPageLocators.COOKIE_OK)