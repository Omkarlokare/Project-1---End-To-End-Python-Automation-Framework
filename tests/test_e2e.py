import json
import time

import pytest

from pageObjects.checkoutPage import checkout
from pageObjects.loginPage import LoginPage
from pageObjects.shopPage import ShopPage

test_data_path = "./test_data/test_e2e.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["Data"]

# @pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance

    loginObj = LoginPage(driver)
    print(loginObj.getTitle())
    shopObj = loginObj.login(test_list_item["username"], test_list_item["password"])

    shopObj.addProductToCard(test_list_item["productName"])
    print(shopObj.getTitle())
    shopObj.goToCart()

    checkoutObj = checkout(driver)
    checkoutObj.clickOnCheckout()

    checkoutObj.enterDeliveryLocation("ind")

    checkoutObj.validateOrder("Success! Thank you!")


