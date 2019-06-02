# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re




class TestCase2FilterStudyProgram(unittest.TestCase):
    def setUp(self):
        print()
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case2_filter_study_program(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("thisispassword")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_id("StudyProgram-btn").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"คณะสถาปัตยกรรมศาสตร์").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"วิทยาลัยแพทยศาสตร์นานาชาติ").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"วิทยาลัยนวัตกรรมการผลิตขั้นสูง").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"คณะครุศาสตร์อุตสาหกรรมและเทคโนโลยี").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"วิทยาลัยอุตสาหกรรมการบินนานาชาติ").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"คณะอุตสาหกรรมเกษตร").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"วิทยาลัยนานาขาติ").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"วิทยาลัยนานาขาติ").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"วิทยาลัยนานาขาติ").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"วิทยาลัยสังคีต").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"วิทยาลัยนาโนเทคโนโลยี").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"วิทยาเขตชุมพรเขตรอุดมศักดิ์").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"วิทยาเขตชุมพรเขตรอุดมศักดิ์").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"คณะวิศวกรรมศาสตร์").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"คณะบริหารและจัดการ").click()
        driver.find_element_by_id("navbarSupportedContent").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"คณะวิทยาศาสตร์").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"คณะเทคโนโลยีสารสนเทศ").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"คณะเทคโนโลยีสารสนเทศ").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"คณะศิลปศาสตร์").click()
        driver.find_element_by_id("navbarDropdown").click()
        driver.find_element_by_link_text(u"คณะเทคโนโลยีการเกษตร").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='admin'])[1]/following::nf[1]").click()
    
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
