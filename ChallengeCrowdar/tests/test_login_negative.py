import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenario:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, passwords, expected_error_message",
                             [("standard_user", "incorrectPassword", "Epic sadface: Username and password do not match any user in this service"),
                              ("locked_out_user", "incorrectPassword", "Epic sadface: Username and password do not match any user in this service"),
                              ("problem_user", "incorrectPassword", "Epic sadface: Username and password do not match any user in this service"),
                              ("performance_glitch_user", "incorrectPassword", "Epic sadface: Username and password do not match any user in this service"),
                              ("", "", "Epic sadface: Username is required"),
                              ("", "incorrectPassword", "Epic sadface: Username is required"),
                              ("standard_user", "", "Epic sadface: Password is required"),
                              ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.")])
    def test_negative_login(self,driver, username, passwords, expected_error_message):
        #Open Browser with URL
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        #Get locators
        username_locator = driver.find_element(By.XPATH,"//input[@id='user-name']")
        password_locator = driver.find_element(By.XPATH,"//input[@id='password']")
        btn_login = driver.find_element(By.XPATH,"//input[@id='login-button']")

        #Input credentials
        username_locator.send_keys(username)
        time.sleep(1)
        password_locator.send_keys(passwords)
        time.sleep(1)
        btn_login.click()

        #Find error message
        error_message_locator = driver.find_element(By.XPATH,"//h3[@data-test='error']")
        assert error_message_locator.is_displayed(), "Error message is not displayed. but it should be"
        errorMessage = error_message_locator.text
        assert errorMessage == expected_error_message, "Error Message is not expected"
        time.sleep(2)

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, passwords",[("problem_user", "secret_sauce")])
    def test_problem_user(self, driver, username, passwords):
        # Open Browser with URL
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        # Get locators
        username_locator = driver.find_element(By.XPATH, "//input[@id='user-name']")
        password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
        btn_login = driver.find_element(By.XPATH, "//input[@id='login-button']")

        # Input credentials
        username_locator.send_keys(username)
        time.sleep(1)
        password_locator.send_keys(passwords)
        time.sleep(1)
        btn_login.click()

        #Ones you log in click on "add to cart" BTN bellow "Sauce Labs Backpack"
        backpack_add_to_cart_locator = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        backpack_add_to_cart_locator.click()
        time.sleep(1)
        #Now try to remove your cart clicking in the "Remove" BTN bellow "Sauce Labs Backpack"
        backpack_remove_locator = driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-backpack']")
        backpack_remove_locator.click()
        time.sleep(1)
        #Verify if the remove BTN is gone.
        if backpack_remove_locator.is_displayed():
            print("This user has issues on the Remove BTN")
        else:
            print("This user has no issues on the Remove BTN")
