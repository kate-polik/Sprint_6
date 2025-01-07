from pages.base_page import BasePage
import allure
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    # Локаторы
    # NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    # SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # METRO_FIELD_LIST_1 = (By.XPATH, "//div[text()='Черкизовская']")
    # METRO_FIELD_LIST_2 = (By.XPATH, "//div[text()='Сокольники']")
    # PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Далее']")
    # DELIVERY_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # DELIVERY_DATE_CHOICE_1 = (By.XPATH,
    #                           "//div[@class='react-datepicker__day react-datepicker__day--001 react-datepicker__day--weekend react-datepicker__day--outside-month']")
    # DELIVERY_DATE_CHOICE_2 = (By.XPATH,
    #                           "//div[@class='react-datepicker__day react-datepicker__day--002 react-datepicker__day--weekend react-datepicker__day--outside-month']")
    # RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    # RENTAL_PERIOD_LIST_1 = (By.XPATH, "//div[text()='двое суток']")
    # RENTAL_PERIOD_LIST_2 = (By.XPATH, "//div[text()='четверо суток']")
    # COLOR_CHECKBOX_1 = (By.XPATH, "//input[@id='black']")
    # COLOR_CHECKBOX_2 = (By.XPATH, "//input[@id='grey']")
    # COMMENT_FIELD = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    # ORDER_BUTTON_FIN = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # ORDER_CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    # SUCCESS_MODAL = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    # VIEW_STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")
    # SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    # YANDEX_LOGO = (By.XPATH, "//img[@src='/assets/ya.svg']")

    # Методы
    @allure.step('Заполнение первой части формы заказа')
    def fill_order_form_part1(self, name, surname, address, metro_locator, phone):
        with allure.step('Ввод имени'):
            self.click_on_element(OrderPageLocators.NAME_FIELD)
            self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)
        with allure.step('Ввод фамилии'):
            self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(surname)
        with allure.step('Ввод адреса'):
            self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)
        with allure.step('Выбор станции метро'):
            self.driver.find_element(*OrderPageLocators.METRO_FIELD).click()
            self.driver.find_element(*metro_locator).click()
        with allure.step('Ввод номера телефона'):
            self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)
        with allure.step('Нажатие кнопки "Далее"'):
            self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнение второй части формы заказа')
    def fill_order_form_part2(self, date_choice, rental_period_list, color_checkbox, comment):
        with allure.step('Выбор даты доставки'):
            self.click_on_element(OrderPageLocators.DELIVERY_DATE_FIELD)
            self.click_on_element(date_choice)
        with allure.step('Выбор срока аренды'):
            self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
            self.click_on_element(rental_period_list)
            self.click_on_element(rental_period_list)
        with allure.step('Выбор цвета самоката'):
            self.click_on_element(color_checkbox)
        with allure.step('Ввод комментария'):
            self.send_keys_to_element(OrderPageLocators.COMMENT_FIELD, comment)
        with allure.step('Оформление заказа'):
            self.click_on_element(OrderPageLocators.ORDER_BUTTON_FIN)
            self.click_on_element(OrderPageLocators.ORDER_CONFIRM_BUTTON)

    @allure.step('Проверка отображения модального окна успешного заказа')
    def is_success_modal_visible(self):
        return self.is_element_visible(OrderPageLocators.SUCCESS_MODAL)

    @allure.step('Нажатие кнопки "Посмотреть статус"')
    def click_view_status(self):
        self.click_on_element(OrderPageLocators.VIEW_STATUS_BUTTON)

    @allure.step('Нажатие на логотип "Самокат"')
    def click_scooter_logo(self):
        self.click_on_element(OrderPageLocators.SCOOTER_LOGO)

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.click_on_element(OrderPageLocators.YANDEX_LOGO)
        with allure.step('Переключение на новую вкладку'):
            self.driver.switch_to.window(self.driver.window_handles[-1])
