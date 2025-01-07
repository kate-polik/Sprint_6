from pages.base_page import BasePage
import allure
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

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
