import time

import pytest
from selenium.webdriver.common.by import By

class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    @pytest.mark.parametrize("username, passwords",[("standard_user", "secret_sauce")])
    def test_positive_login(self, driver,username,passwords):
        # Go to webpage
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        # Get locators
        username_locator = driver.find_element(By.XPATH,"//input[@id='user-name']")
        password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
        btnLogin = driver.find_element(By.XPATH, "//input[@id='login-button']")
        time.sleep(2)

        #Input credentials
        username_locator.send_keys(username)
        time.sleep(1)
        password_locator.send_keys(passwords)
        time.sleep(1)
        btnLogin.click()

        #Verify Add to Cart BTN is displayed
        backpack_add_to_cart_locator = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        assert backpack_add_to_cart_locator.is_displayed()
        print("Login was correctly done")

    @pytest.mark.login
    @pytest.mark.positive
    @pytest.mark.parametrize("username, passwords, name, last_name, postal_code",[("standard_user", "secret_sauce", "juan", "munoz", "7000")])
    def test_positive_add(self, driver,username,passwords,name,last_name,postal_code):
        # Go to webpage
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        # Get locators
        username_locator = driver.find_element(By.XPATH,"//input[@id='user-name']")
        password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
        btnLogin = driver.find_element(By.XPATH, "//input[@id='login-button']")
        time.sleep(2)

        #Input credentials
        username_locator.send_keys(username)
        time.sleep(1)
        password_locator.send_keys(passwords)
        time.sleep(1)
        btnLogin.click()

        #Add to cart backpack and The bike lights
        backpack_add_to_cart_locator = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        backpack_add_to_cart_locator.click()
        bike_lights_locator = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']")
        bike_lights_locator.click()
        time.sleep(1)

        #Enter to the Cart page
        cart_btn_locator = driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']")
        cart_btn_locator.click()
        time.sleep(1)
        #Ones you are inside click on Checkout BTN
        checkout_btn_locator = driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn_locator.click()
        time.sleep(1)
        #Input name, last name and postal code
        first_name_locator = driver.find_element(By.XPATH,"//input[@id='first-name']")
        last_name_locator = driver.find_element(By.XPATH, "//input[@id='last-name']")
        postal_code_locator = driver.find_element(By.XPATH, "//input[@id='postal-code']")

        first_name_locator.send_keys(name)
        last_name_locator.send_keys(last_name)
        postal_code_locator.send_keys(postal_code)
        time.sleep(2)
        #Click on continue BTN
        continue_btn_locator = driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn_locator.click()
        time.sleep(1)
        #Click on Finish BTN
        finish_btn_locator = driver.find_element(By.XPATH,"//button[@id='finish']")
        finish_btn_locator.click()
        #verify "Thank you for your order!" message
        order_complete_locator = driver.find_element(By.XPATH,"//h2[@class='complete-header']")
        assert order_complete_locator.is_displayed(), "Your order has not been completed"
        orderMessage = order_complete_locator.text
        assert orderMessage == "Thank you for your order!", "Order Message is not expected"
        time.sleep(2)