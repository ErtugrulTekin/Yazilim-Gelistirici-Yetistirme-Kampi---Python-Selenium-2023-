from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By 

class Test_Cases:
    def case1(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        login = driver.find_element(By.ID, "login-button")
        login.click()
        
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"1.Test Sonucu: {testResult}")

    def case2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        emailInput = driver.find_element(By.ID, "user-name")
        emailInput.send_keys("1")

        login = driver.find_element(By.ID, "login-button")
        login.click()

        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"2.Test Sonucu: {testResult}")

    def case3(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        emailInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")

        emailInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")

        login = driver.find_element(By.ID, "login-button")
        login.click()

        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"3.Test Sonucu: {testResult}")

    def case4(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        login = driver.find_element(By.ID, "login-button")
        login.click()
        
        usernameIcon = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        usernameIconEnabled = usernameIcon.is_enabled()
        print(f"Kullanici hata ikonu var mi: {usernameIconEnabled}")

        passwordIcon = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        passwordIconEnabled = passwordIcon.is_enabled()
        print(f"Sifre hata ikonu var mi: {passwordIconEnabled}")

        errorMessageButton = driver.find_element(By.CLASS_NAME, "error-button")
        varMi = errorMessageButton.is_enabled()
        print(f"Hata mesaji kapatma butonu var mi: {varMi}")
        errorMessageButton.click()
        
        #login.click() yapmadan önce ikonları bulmaya çalıştığımda sistem hata veriyor ama 
        #login.Click() yaptığımda ikonlar ekranda çıktığı için True sonucunu alıyorum.
        #Bu şekilde bir kontrol sağlamış oldum.

    def case5(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        emailInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")

        emailInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")

        login = driver.find_element(By.ID, "login-button")
        login.click()
        print("Inventory sitesine gecis yapildi")

    def case6(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        emailInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")

        emailInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")

        login = driver.find_element(By.ID, "login-button")
        login.click()
        print("Inventory sitesine gecis yapildi")

        listOfInventory = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Inventory sitesinde şu anda {len(listOfInventory)} adet ürün sayisi var.")


testClass = Test_Cases()
#testClass.case1()
#testClass.case2()
#testClass.case3()
#testClass.case4()
#testClass.case5()
#testClass.case6()

#Hepsi kontrol edildi ve çalıştı