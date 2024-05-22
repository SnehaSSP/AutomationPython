from selenium import webdriver
from selenium.webdriver.common.by import By

from LoginAutomation22May.utils.config import BASE_URL, USERNAME, PASSWORD


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "i.fa.fa-2x.fa-sign-in")

    def open_browser(self):
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

    def login(self):
        self.driver.find_element(*self.username_field).send_keys(USERNAME)
        self.driver.find_element(*self.password_field).send_keys(PASSWORD)
        self.driver.find_element(*self.login_button).click()

