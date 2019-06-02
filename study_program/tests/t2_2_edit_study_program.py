# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re




class TestCase2EditStudyProgram(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 2-2: other activities for study program ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case2_edit_study_program(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("thisispassword")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::b[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='ENGAGIRCULBMT : หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมเกษตร'])[1]/following::h6[2]").click()
        driver.find_element_by_id("studyProgram-btn").click()
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("GOING TO CLOSE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("studyProgram-btn").click()
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("NOT ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("studyProgram-btn").click()
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("GOING TO CLOSE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("studyProgram-btn").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program supported by other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("studyProgram-btn").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Collaborated program with other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("studyProgram-btn").click()
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("NOT ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("studyProgram-btn").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program supported by other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("studyProgram-btn").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Collaborated program with other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_link_text("docs_link").click()
        time.sleep(0.5)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        driver.find_element_by_link_text("study program").click()
        time.sleep(0.5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='AGTAGRICULDMT : หลักสูตรปรัชญาดุษฎีบัณฑิต สาขาวิชาเกษตรศาสตร์'])[1]/following::i[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='SCIPETROCHBNI : หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาปิโตรเคมี (หลักสูตรนานาชาติ)'])[1]/following::a[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='AGTAGRICULDMT : หลักสูตรปรัชญาดุษฎีบัณฑิต สาขาวิชาเกษตรศาสตร์'])[1]/following::i[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='SCIPETROCHBNI : หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาปิโตรเคมี (หลักสูตรนานาชาติ)'])[1]/following::i[2]").click()
        driver.find_element_by_id("studyProgram-btn").click()
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
