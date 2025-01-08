import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.feature('Раздел "Вопросы о важном"')
@allure.title('Тест функциональности выпадающего списка "Вопросы о важном"')
@pytest.mark.parametrize(
    "faq_item",
    MainPageLocators.FAQ_ITEMS
)
def test_faq_dropdown(driver, faq_item):
    faq_page = MainPage(driver)
    faq_page.click_on_cookie()
    faq_page.scroll_to_element(faq_item["question"])
    faq_page.click_on_element(faq_item["question"])
    assert faq_page.is_element_visible(faq_item["answer"]), "Ответ не отображается"
