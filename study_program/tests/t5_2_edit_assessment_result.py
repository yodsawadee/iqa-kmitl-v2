# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCase5EditAssessmentResult(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 5-2: other activities for assessment result ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case5_edit_assessment_result(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("thisispassword")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Professors(อาจารย์)___________________'])[1]/following::b[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::b[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Export องค์1 CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("assessment-btn").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='AAI: วิทยาลัยอุตสาหกรรมการบินนานาชาติ'])[1]/following::h6[1]").click()
        driver.find_element_by_id("assessment-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_committee_id | label=2561 : วสุ อุดมเพทายกุล]]
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_committee_id | label=2561 : วิบูลย์ พร้อมพานิชย์]]
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_committee_id | label=2561 : จันทนี เพชรานนท์]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Committee id'])[1]/following::option[3]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_committee_id | label=2561 : วิบูลย์ พร้อมพานิชย์]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Committee id'])[1]/following::option[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pdf docs link'])[1]/following::input[2]").click()
        driver.find_element_by_id("assessment-btn").click()
        driver.find_element_by_id("id_curriculum_status").click()
        Select(driver.find_element_by_id("id_curriculum_status")).select_by_visible_text("Modify")
        driver.find_element_by_id("id_curriculum_status").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pdf docs link'])[1]/following::input[2]").click()
        driver.find_element_by_id("assessment-btn").click()
        driver.find_element_by_id("id_curriculum_status").click()
        Select(driver.find_element_by_id("id_curriculum_status")).select_by_visible_text("New")
        driver.find_element_by_id("id_curriculum_status").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pdf docs link'])[1]/following::input[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Edit Assessment Result'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_criteria1").clear()
        driver.find_element_by_id("id_criteria1").send_keys("2")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_criteria2").clear()
        driver.find_element_by_id("id_criteria2").send_keys("2")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_criteria3").clear()
        driver.find_element_by_id("id_criteria3").send_keys("2")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_criteria4").clear()
        driver.find_element_by_id("id_criteria4").send_keys("2")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_criteria5").clear()
        driver.find_element_by_id("id_criteria5").send_keys("2")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_criteria6").clear()
        driver.find_element_by_id("id_criteria6").send_keys("2")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_criteria7").clear()
        driver.find_element_by_id("id_criteria7").send_keys("2")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_criteria8").clear()
        driver.find_element_by_id("id_criteria8").send_keys("2")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Edit Assessment Result'])[1]/following::div[2]").click()
        driver.find_element_by_id("id_criteria9").clear()
        driver.find_element_by_id("id_criteria9").send_keys("2")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_criteria10").clear()
        driver.find_element_by_id("id_criteria10").send_keys("2")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_criteria11").clear()
        driver.find_element_by_id("id_criteria11").send_keys("2")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_total_score").clear()
        driver.find_element_by_id("id_total_score").send_keys("2")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[13]/following::input[2]").click()
        driver.find_element_by_link_text("docs_link").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        time.sleep(0.5)
        driver.find_element_by_id("nav-text").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='admin'])[1]/following::nf[1]").click()
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
