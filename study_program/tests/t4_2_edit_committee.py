# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCase4EditCommittee(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 4-2: other activities for committee ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case4_edit_committee(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("thisispassword")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Professors(อาจารย์)___________________'])[1]/following::b[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='AssessmentResults(ผลการประเมิน)___________________'])[1]/following::b[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Add Committee'])[1]/following::h6[5]").click()
        driver.find_element_by_id("committee-btn").click()
        driver.find_element_by_id("id_assessment_level").click()
        Select(driver.find_element_by_id("id_assessment_level")).select_by_visible_text("Junior")
        driver.find_element_by_id("id_assessment_level").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Assessment programs'])[1]/following::input[1]").click()
        driver.find_element_by_id("committee-btn").click()
        driver.find_element_by_id("id_assessment_level").click()
        Select(driver.find_element_by_id("id_assessment_level")).select_by_visible_text("Senior")
        driver.find_element_by_id("id_assessment_level").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Assessment programs'])[1]/following::input[1]").click()
        driver.find_element_by_id("committee_detail-container-title").click()
        driver.find_element_by_id("committee-btn").click()
        driver.find_element_by_id("id_assessment_level").click()
        Select(driver.find_element_by_id("id_assessment_level")).select_by_visible_text("Novice")
        driver.find_element_by_id("id_assessment_level").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Assessment programs'])[1]/following::input[1]").click()
        driver.find_element_by_id("committee-btn").click()
        driver.find_element_by_id("id_assessment_level").click()
        Select(driver.find_element_by_id("id_assessment_level")).select_by_visible_text("Apprentice-C")
        driver.find_element_by_id("id_assessment_level").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Assessment programs'])[1]/following::input[1]").click()
        driver.find_element_by_id("committee-btn").click()
        driver.find_element_by_id("id_assessment_level").click()
        Select(driver.find_element_by_id("id_assessment_level")).select_by_visible_text("Senior")
        driver.find_element_by_id("id_assessment_level").click()
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_profession").clear()
        driver.find_element_by_id("id_profession").send_keys("engineer")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Assessment programs'])[1]/following::input[1]").click()
        driver.find_element_by_id("committee-btn").click()
        driver.find_element_by_id("id_year").click()
        Select(driver.find_element_by_id("id_year")).select_by_visible_text("2562")
        driver.find_element_by_id("id_year").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Assessment programs'])[1]/following::input[1]").click()
        driver.find_element_by_id("committee-btn").click()
        driver.find_element_by_id("id_year").click()
        Select(driver.find_element_by_id("id_year")).select_by_visible_text("2561")
        driver.find_element_by_id("id_year").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Assessment programs'])[1]/following::input[1]").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("all committee").click()
        time.sleep(0.5)
        driver.find_element_by_id("committee-btn").click()
        time.sleep(0.5)
        driver.find_element_by_id("sign-out-alt").click()
    
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
