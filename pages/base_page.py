import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввод текста в элемент")
    def send_keys_to_element(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    @allure.step("Переключение на последнее открытое окно")
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидание конкретного URL")
    def wait_for_url(self, url, timeout=12):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))
