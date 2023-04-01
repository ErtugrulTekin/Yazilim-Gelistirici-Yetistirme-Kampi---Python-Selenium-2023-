from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_Cases:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
    
    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))   

    def test_case1(self):
        login = self.driver.find_element(By.ID, "login-button")
        login.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-case1.png")
        assert errorMessage.text == "Epic sadface: Username is required"
    
    @pytest.mark.parametrize("username", [("1")])
    def test_case2(self,username):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(username)

        login = self.driver.find_element(By.ID, "login-button")
        login.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container'  ]/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-case2-{username}.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    @pytest.mark.parametrize("username,password", [("locked_out_user","secret_sauce")])
    def test_case3(self,username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),10)
        passwordInput = self.driver.find_element(By.ID, "password")
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        login = self.driver.find_element(By.ID, "login-button")
        login.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container'  ]/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-case3-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out." 

    def test_case4(self):
        login = self.driver.find_element(By.ID, "login-button")
        login.click()

        self.waitForElementVisible((By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg"))
        usernameIcon = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        self.waitForElementVisible((By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg"))
        passwordIcon = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        self.waitForElementVisible((By.CLASS_NAME, "error-button"))
        errorMessageButton = self.driver.find_element(By.CLASS_NAME, "error-button")
        self.driver.save_screenshot(f"{self.folderPath}/test-case4.png")
        errorMessageButton.click()

    @pytest.mark.parametrize("username,password", [("standard_user","secret_sauce")])
    def test_case5(self,username,password):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),10)
        passwordInput = self.driver.find_element(By.ID, "password")
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        login = self.driver.find_element(By.ID, "login-button")
        login.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-case5-{username}-{password}.png")

    @pytest.mark.parametrize("username,password", [("standard_user","secret_sauce")])
    def test_case6(self,username,password):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),10)
        passwordInput = self.driver.find_element(By.ID, "password")
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        login = self.driver.find_element(By.ID, "login-button")
        login.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-case6-{username}-{password}.png")
        listOfInventory = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(listOfInventory) == 6

    @pytest.mark.parametrize("username,password", [("standard_user","secret_sauce")])
    def test_case7(self,username,password):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),10)
        passwordInput = self.driver.find_element(By.ID, "password")
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        login = self.driver.find_element(By.ID, "login-button")
        login.click()

        self.waitForElementVisible((By.ID, "react-burger-menu-btn"))
        menu = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu.click()

        self.waitForElementVisible((By.ID, "about_sidebar_link"))
        aboutButton = self.driver.find_element(By.ID, "about_sidebar_link")
        aboutButton.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-case7-{username}-{password}.png")

    @pytest.mark.parametrize("username,password", [("standard_user","secret_sauce")])
    def test_case8(self,username,password):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),10)
        passwordInput = self.driver.find_element(By.ID, "password")
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        login = self.driver.find_element(By.ID, "login-button")
        login.click()

        self.waitForElementVisible((By.CLASS_NAME, "product_sort_container"))
        filterButton = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        filterButton.click()
        
        self.waitForElementVisible((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[4]"))
        priceButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[4]")
        priceButton.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-case8-Price(high to low).png")

        self.waitForElementVisible((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))
        addToCartButton = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        addToCartButton.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-case8-addToCartButton.png")

        self.waitForElementVisible((By.CLASS_NAME, "shopping_cart_link"))
        basketButton = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        basketButton.click()

        self.waitForElementVisible((By.ID, "remove-sauce-labs-fleece-jacket"))
        deleteButton = self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket")
        deleteButton.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-case8-deleteButton.png")

    @pytest.mark.parametrize("username,password,firstname,lastname", [("standard_user","secret_sauce","Ali","Can")])
    def test_case9(self,username,password,firstname,lastname):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),10)
        passwordInput = self.driver.find_element(By.ID, "password")
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        login = self.driver.find_element(By.ID, "login-button")
        login.click()

        self.waitForElementVisible((By.CLASS_NAME, "shopping_cart_link"))
        basketButton = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        basketButton.click()

        self.waitForElementVisible((By.ID, "checkout"))
        checkoutButton = self.driver.find_element(By.ID, "checkout")
        checkoutButton.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-case9-Checkout.png")

        self.waitForElementVisible((By.ID, "first-name"))
        firstnameInput = self.driver.find_element(By.ID, "first-name")
        self.waitForElementVisible((By.ID, "last-name"))
        lastnameInput = self.driver.find_element(By.ID, "last-name")

        firstnameInput.send_keys(firstname)
        lastnameInput.send_keys(lastname)

        continueButton = self.driver.find_element(By.ID, "continue")
        continueButton.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-case9-{username}-{password}-{firstname}-{lastname}.png")
        assert errorMessage.text == "Error: Postal Code is required"


        


        


