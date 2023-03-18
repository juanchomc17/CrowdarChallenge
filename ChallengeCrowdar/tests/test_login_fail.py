import time

import pytest
from selenium.webdriver.common.by import By

class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.fail
    @pytest.mark.parametrize("username, passwords",[("standard_user", "")])
    def test_fail_login(self, driver,username,passwords):
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

        #It's going to verify to change the URL to be https://www.saucedemo.com/inventory.html, but It's going to fail because it won't log in!
        assert driver.title == "https://www.saucedemo.com/inventory.html"
