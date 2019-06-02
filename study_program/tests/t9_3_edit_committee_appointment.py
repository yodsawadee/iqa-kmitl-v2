# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCase9EditCommitteeAppointment(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 9-3: edit committee appointment / solve appointment conflict ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case9_edit_committee_appointment(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("mse")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("mse")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Assessment(การประเมินผล)___________________'])[1]/following::b[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)=concat('Faculty', \"'\", 'sStudy Program(หลักสูตรในคณะ)___________________')])[1]/following::b[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create Appointment'])[1]/following::h6[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_appointed_committee | label=2561 : วิบูลย์ พร้อมพานิชย์]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Appointed committee'])[1]/following::option[3]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_appointed_committee | label=2561 : นคร ศรีสุขุมบวรชัย]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Appointed committee'])[1]/following::option[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[4]/following::input[2]").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_xpath("//div[@id='login-container']/div").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("adm")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("adm")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_id("Faculty-btn").click()
        driver.find_element_by_id("Appointment-btn").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create Appointment'])[1]/following::h6[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_appointed_committee | label=2561 : วสุ อุดมเพทายกุล]]
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_appointed_committee | label=2561 : จันทนี เพชรานนท์]]
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_appointed_committee | label=2561 : นคร ศรีสุขุมบวรชัย]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Appointed committee'])[1]/following::option[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_appointed_committee | label=2561 : ชัยวัฒน์ หนูทอง]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Appointed committee'])[1]/following::option[5]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[4]/following::input[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='adm'])[1]/following::nf[1]").click()
    
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
