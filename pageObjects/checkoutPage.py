from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserUtils import browUtils


class checkout(browUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.checkoutClick = (By.CSS_SELECTOR, "button[class='btn btn-success']")
        self.inputCountryName = (By.ID, "country")
        self.countryOptions = (By.LINK_TEXT, "India")
        self.selectCountry = (By.LINK_TEXT, "India")
        self.checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchase = (By.CSS_SELECTOR, "input[type='submit']")
        self.assertionText = (By.CLASS_NAME, "alert-success")


    def clickOnCheckout(self):
        self.driver.find_element(*self.checkoutClick).click()


    def enterDeliveryLocation(self,country_name):
        self.driver.find_element(*self.inputCountryName).send_keys(country_name)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.countryOptions))
        self.driver.find_element(*self.selectCountry).click()

        self.driver.find_element(*self.checkBox).click()
        self.driver.find_element(*self.purchase).click()




    def validateOrder(self,assertText):
        successText = self.driver.find_element(*self.assertionText).text
        assert assertText in successText
