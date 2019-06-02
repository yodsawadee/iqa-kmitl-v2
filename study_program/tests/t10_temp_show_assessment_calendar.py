# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UTestCase10ShowAssessmentCalendar(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 10: show assessment calendar ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_u_test_case10_show_assessment_calendar(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("thisispassword")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_id("IQA-btn").click()
        driver.find_element_by_id("Calendar-btn").click()
        driver.find_element_by_link_text("7").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_link_text("8").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_link_text("9").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_link_text("10").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sun'])[1]/following::i[7]").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_link_text("12").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_id("exclamation-circle-icon").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='June 2562'])[1]/following::i[1]").click()
        driver.find_element_by_id("af-circle-icon").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='June 2562'])[1]/following::a[1]").click()
        driver.find_element_by_link_text("29").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='June 2562'])[1]/following::i[1]").click()
        driver.find_element_by_link_text("21").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='June 2562'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::h2[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::h2[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='July 2562'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='August 2562'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='September 2562'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='October 2562'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='November 2562'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='December 2562'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='January 2563'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='February 2563'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/following::nf[1]").click()
        driver.find_element_by_link_text("Logout").click()
    
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
