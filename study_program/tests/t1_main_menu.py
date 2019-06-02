# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium import webdriver



# chromedriver = "./chromedriver"
# self.driver = webdriver.Chrome(chromedriver)


class TestCase1MainMenu(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 1: main menu ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case1_main_menu(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("thisispassword")
        time.sleep(0.5)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        time.sleep(0.5)
        driver.find_element_by_id("StudyProgram-btn").click()
        time.sleep(0.5)
        driver.find_element_by_id("nav-text").click()
        time.sleep(0.5)
        driver.find_element_by_id("Professors-btn").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='IQA Menu'])[1]/preceding::nf[1]").click()
        time.sleep(0.5)
        driver.find_element_by_id("Assessment-btn").click()
        time.sleep(0.5)
        driver.find_element_by_id("AssessmentResults-btn").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='IQA Menu'])[1]/preceding::nf[1]").click()
        time.sleep(0.5)
        driver.find_element_by_id("Assessment-btn").click()
        time.sleep(0.5)
        driver.find_element_by_id("CommitteeList-btn").click()
        time.sleep(0.5)
        driver.find_element_by_id("nav-text").click()
        time.sleep(0.5)
        driver.find_element_by_id("sign-out-alt").click()
        time.sleep(0.5)
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    