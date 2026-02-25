from selenium.webdriver.common.by import By

from pageObjects.shopPage import ShopPage
from utils.browserUtils import browUtils


class LoginPage(browUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.user_input = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signIn = (By.ID, "signInBtn")

    def login(self,username, password):
        self.driver.find_element(*self.user_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signIn).click()
        shopObj = ShopPage(self.driver)
        return shopObj





