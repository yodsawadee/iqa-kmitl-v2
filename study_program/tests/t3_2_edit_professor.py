# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCase3EditProfessor(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 3-2: other activities for professor ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case3_edit_professor(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='IQA System'])[1]/following::form[1]").click()
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("thisispassword")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Study Program(หลักสูตร)___________________'])[1]/following::b[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='อ. วิบูลย์ พร้อมพานิชย์'])[1]/following::h6[2]").click()
        driver.find_element_by_id("professor-btn").click()
        driver.find_element_by_id("id_date_of_birth").click()
        driver.find_element_by_id("id_date_of_birth").clear()
        driver.find_element_by_id("id_date_of_birth").send_keys("2549-06-25")
        driver.find_element_by_id("id_bsc").click()
        driver.find_element_by_id("id_bsc").clear()
        driver.find_element_by_id("id_bsc").send_keys(u"วิศวะไฟฟ้า")
        driver.find_element_by_id("id_bsc_grad_institute").click()
        driver.find_element_by_id("id_bsc_grad_institute").clear()
        driver.find_element_by_id("id_bsc_grad_institute").send_keys("KMITL")
        driver.find_element_by_id("id_bsc_year").click()
        driver.find_element_by_id("id_bsc_year").click()
        driver.find_element_by_id("id_msc").click()
        driver.find_element_by_id("id_msc").clear()
        driver.find_element_by_id("id_msc").send_keys(u"วิศวะเครื่องกล")
        driver.find_element_by_id("id_msc_grad_institute").click()
        driver.find_element_by_id("id_msc_grad_institute").clear()
        driver.find_element_by_id("id_msc_grad_institute").send_keys("KMITL")
        driver.find_element_by_id("id_msc_year").click()
        Select(driver.find_element_by_id("id_msc_year")).select_by_visible_text("2552")
        driver.find_element_by_id("id_msc_year").click()
        driver.find_element_by_id("id_phd").click()
        driver.find_element_by_id("id_phd").clear()
        driver.find_element_by_id("id_phd").send_keys(u"วิศวะควบคุม")
        driver.find_element_by_id("id_phd_grad_institute").click()
        driver.find_element_by_id("id_phd_grad_institute").clear()
        driver.find_element_by_id("id_phd_grad_institute").send_keys("TUM")
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_id("id_phd_year").click()
        Select(driver.find_element_by_id("id_phd_year")).select_by_visible_text("2556")
        driver.find_element_by_id("id_phd_year").click()
        driver.find_element_by_id("id_phone").click()
        driver.find_element_by_id("id_phone").clear()
        driver.find_element_by_id("id_phone").send_keys("0811234567")
        driver.find_element_by_id("id_email").click()
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("kochaiwat@kmitl.ac.th")
        driver.find_element_by_id("id_university").click()
        driver.find_element_by_id("id_university").clear()
        driver.find_element_by_id("id_university").send_keys("KMITL")
        driver.find_element_by_id("id_additional_degree").click()
        driver.find_element_by_id("id_additional_degree").clear()
        driver.find_element_by_id("id_additional_degree").send_keys("-")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาการจัดการโลจิสติกส์ (หลักสูตรนานาชาติ)]]
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_responsible_program | label=หลักสูตรบริหารธุรกิจบัณฑิต (หลักสูตรนานาชาติ)]]
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_responsible_program | label=หลักสูตรครุศาสตร์อุตสาหกรรมบัณฑิต สาขาวิชาครุศาสตร์เกษตร]]
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_responsible_program | label=หลักสูตรปรัชญาดุษฎีบัณฑิต สาขาวิชาเกษตรศาสตร์]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[6]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::input[1]").click()
        driver.find_element_by_link_text("all professor").click()
        driver.find_element_by_id("professor-btn").click()
        driver.find_element_by_link_text("home").click()
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
