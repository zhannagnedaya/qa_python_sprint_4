import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.locator_ya_logo).click()

    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.locator_scooter_logo).click()

    @allure.step('Клик по кнопке да все привыкли в сообщении И здесь куки! В общем, мы их используем.')
    def click_close_cookie(self):
        self.driver.find_element(*MainPageLocators.locator_cookie_button).click()

    @allure.step('Клик по кнопке Заказать вверху страницы')
    def click_first_order_button(self):
        self.driver.find_elements(*MainPageLocators.locator_order_button)[0].click()

    @allure.step('Клик по кнопке Заказать внизу страницы')
    def click_second_order_button(self):
        self.driver.find_elements(*MainPageLocators.locator_order_button)[2].click()

    @allure.step('Клик по Сколько это стоит? И как оплатить? в блоке Вопросы о важном')
    def click_question_one(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 15).until(
            ec.visibility_of_element_located(MainPageLocators.locator_question_one_element))
        element.click()

    @allure.step('Клик по Хочу сразу несколько самокатов! Так можно? в блоке Вопросы о важном')
    def click_question_two(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located(MainPageLocators.locator_question_two_element))
        element.click()

    @allure.step('Клик по Как рассчитывается время аренды? в блоке Вопросы о важном')
    def click_question_three(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located(MainPageLocators.locator_question_three_element))
        element.click()

    @allure.step('Клик по Можно ли заказать самокат прямо на сегодня? в блоке Вопросы о важном')
    def click_question_four(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located(MainPageLocators.locator_question_four_element))
        element.click()

    @allure.step('Клик по Можно ли продлить заказ или вернуть самокат раньше? в блоке Вопросы о важном')
    def click_question_five(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located(MainPageLocators.locator_question_five_element))
        element.click()

    @allure.step('Клик по Вы привозите зарядку вместе с самокатом? в блоке Вопросы о важном')
    def click_question_six(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located(MainPageLocators.locator_question_six_element))
        element.click()

    @allure.step('Клик по Можно ли отменить заказ? в блоке Вопросы о важном')
    def click_question_seven(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located(MainPageLocators.locator_question_seven_element))
        element.click()

    @allure.step('Клик по Я жизу за МКАДом, привезёте? в блоке Вопросы о важном')
    def click_question_eight(self):
        last_element = self.driver.find_element(*MainPageLocators.locator_question_eight_element)
        self.driver.execute_script('arguments[0].scrollIntoView();', last_element)
        element = WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located(MainPageLocators.locator_question_eight_element))
        element.click()

    @allure.step('Ответ на вопрос Сколько это стоит? И как оплатить? в блоке Вопросы о важном')
    def get_answer_one(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(*MainPageLocators.locator_answer_one_element)).text

    @allure.step('Ответ на вопрос Хочу сразу несколько самокатов! Так можно? в блоке Вопросы о важном')
    def get_answer_two(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_answer_two_element)).text

    @allure.step('Ответ на вопрос Как рассчитывается время аренды? в блоке Вопросы о важном')
    def get_answer_three(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_answer_three_element)).text

    @allure.step('Ответ на вопрос Можно ли заказать самокат прямо на сегодня? в блоке Вопросы о важном')
    def get_answer_four(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(MainPageLocators.locator_answer_four_element)).text

    @allure.step('Ответ на вопрос Можно ли продлить заказ или вернуть самокат раньше? в блоке Вопросы о важном')
    def get_answer_five(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(MainPageLocators.locator_answer_five_element)).text

    @allure.step('Ответ на вопрос Вы привозите зарядку вместе с самокатом? в блоке Вопросы о важном')
    def get_answer_six(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(MainPageLocators.locator_answer_six_element)).text

    @allure.step('Ответ на вопрос Можно ли отменить заказ? в блоке Вопросы о важном')
    def get_answer_seven(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(MainPageLocators.locator_answer_seven_element)).text

    @allure.step('Ответ на вопрос Я жизу за МКАДом, привезёте? в блоке Вопросы о важном')
    def get_answer_eight(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(MainPageLocators.locator_answer_eight_element)).text