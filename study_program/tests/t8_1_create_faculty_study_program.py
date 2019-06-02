# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCase8CreateFacultyStudyProgram(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 8-1: create faculty study program ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case8_create_faculty_study_program(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("eng")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("eng")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_id("Faculty-btn").click()
        driver.find_element_by_id("StudyProgram2-btn").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("ENGCHEMICABMT")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมเคมี")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"วิศวกรรมศาสตรบัณฑิต (วิศวกรรมเคมี)")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_professors | label=ชัยวัฒน์ หนูทอง]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::option[8]").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/open?id=1Natq0Adfye6GojZbgsjlguF6VecGZH4c")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("nav-text").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='eng'])[1]/following::nf[1]").click()
    
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
