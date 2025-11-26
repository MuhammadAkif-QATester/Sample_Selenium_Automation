import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

@allure.feature("Zoneomics")
class Zoneomics(unittest.TestCase):
    @classmethod
    def setUp(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        self.driver.quit()


    @allure.story("Testing the login")
    def test_checking_login_of_zoneomics(self):
        self.driver.get("https://zoneomics.com")
        self.driver.implicitly_wait(20)
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Log in']")))
        self.driver.find_element(By.XPATH, "//a[text()='Log in']").click()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']")))
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("m.akif@zoneomics.com")
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("corelogic")
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        try:
            WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome Back')]")))
            assert True
        except:
            assert False


