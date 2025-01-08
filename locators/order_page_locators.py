from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поля формы заказа
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_FIELD_LIST_1 = (By.XPATH, "//div[text()='Черкизовская']")
    METRO_FIELD_LIST_2 = (By.XPATH, "//div[text()='Сокольники']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Далее']")
    DELIVERY_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DELIVERY_DATE_CHOICE_1 = (By.XPATH,
                              "//div[@class='react-datepicker__day react-datepicker__day--001 react-datepicker__day--weekend react-datepicker__day--outside-month']")
    DELIVERY_DATE_CHOICE_2 = (By.XPATH,
                              "//div[@class='react-datepicker__day react-datepicker__day--002 react-datepicker__day--weekend react-datepicker__day--outside-month']")
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    RENTAL_PERIOD_LIST_1 = (By.XPATH, "//div[text()='двое суток']")
    RENTAL_PERIOD_LIST_2 = (By.XPATH, "//div[text()='четверо суток']")
    COLOR_CHECKBOX_1 = (By.XPATH, "//input[@id='black']")
    COLOR_CHECKBOX_2 = (By.XPATH, "//input[@id='grey']")
    COMMENT_FIELD = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    ORDER_BUTTON_FIN = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    ORDER_CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    SUCCESS_MODAL = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@src='/assets/ya.svg']")