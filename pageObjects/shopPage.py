from selenium.webdriver.common.by import By

from utils.browserUtils import browUtils


class ShopPage(browUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.clickShop = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product = (By.XPATH, "//div[@class='card h-100']")
        self.goToCartButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")



    def addProductToCard(self,actProductName):

        self.driver.find_element(*self.clickShop).click()

        products = self.driver.find_elements(*self.product)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == actProductName:
                product.find_element(By.XPATH, "div/button").click()


    def goToCart(self):
        self.driver.find_element(*self.goToCartButton).click()

