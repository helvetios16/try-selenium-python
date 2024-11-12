import time
import pytest
from selenium.webdriver.common.by import By


class TestRegisterPage:
    def test_valid_register(self, driver):
        driver.get("http://localhost:4321/register")

        driver.find_element(By.ID, "name").send_keys("Crishtian")
        driver.find_element(By.ID, "paternalName").send_keys("Jose")
        driver.find_element(By.ID, "maternalName").send_keys("Maria")
        driver.find_element(By.ID, "date-of-birth").send_keys("10/09/2000")
        driver.find_element(By.ID, "user").send_keys("juan6")
        driver.find_element(By.ID, "email").send_keys("juan6@gmail.com")
        driver.find_element(By.ID, "password").send_keys("123456")

        driver.find_element(By.ID, "form-register").submit()

        time.sleep(1)
        currentUrl = driver.current_url
        assert currentUrl == "http://localhost:4321/"
