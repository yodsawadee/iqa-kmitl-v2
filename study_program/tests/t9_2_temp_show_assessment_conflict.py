# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCase9DEMPShowConflict(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 9-2: show appointment conflict ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case9_d_e_m_p_show_conflict(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("mse")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("mse")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_id("Faculty-btn").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='IQA CommitteeAppointment(การนัดกรรมการ)___________________'])[1]/following::b[2]").click()
        driver.find_element_by_link_text("10").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_link_text("11").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_link_text("12").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_link_text("9").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_link_text("8").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_link_text("7").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='June 2562'])[1]/following::a[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::i[1]").click()
        driver.find_element_by_id("exclamation-circle-icon").click()
        driver.find_element_by_link_text("assessment calendar").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/following::nf[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='mse'])[1]/following::nf[1]").click()
    
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
