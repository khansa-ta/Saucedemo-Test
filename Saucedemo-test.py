from cgitb import text
from lib2to3.pgen2 import driver
import unittest
import time
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Test_a_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_Login_Failed(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("khansa")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys(12345678)
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

        response_message = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button").text
        self.assertIn(response_message,"Username and password do not match")
     
    def test_b_Login_Successful(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

        response_data= driver.find_element(By.ID,"page_wrapper")
    
    def test_c_Login_EmptyUser(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

        response_message = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button").text
        self.assertIn(response_message,"Username is required")
    
    def test_d_Login_EmptyPass(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

        response_message = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button").text
        self.assertIn(response_message,"Password is required")

class Test_b_AddtoCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_AddtoCart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()
        
        response_message = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
        self.assertEqual(response_message, "1")

    def tearDown(self): 
        self.driver.close() 

unittest.main()

    