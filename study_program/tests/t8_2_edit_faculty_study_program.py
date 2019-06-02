# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCase8EditFacultyStudyProgram(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 8-2: other activities for faculty study program ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case8_edit_faculty_study_program(self):
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
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='ENGAGIRCULBMT : หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมเกษตร'])[1]/following::h6[2]").click()
        driver.find_element_by_id("facultyStudyProgram-btn").click()
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program supported by other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("facultyStudyProgram-btn").click()
        driver.find_element_by_id("div_id_pdf_docs").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Collaborated program with other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("facultyStudyProgram-btn").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("facultyStudyProgram-btn").click()
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("GOING TO CLOSE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("facultyStudyProgram-btn").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Collaborated program with other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program supported by other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1] | ]]
        driver.find_element_by_id("facultyStudyProgram-btn").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Collaborated program with other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("facultyStudyProgram-btn").click()
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("facultyStudyProgram-btn").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program supported by other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_id("facultyStudyProgram-btn").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Edit Faculty Study Program'])[1]/following::form[1]").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Collaborated program with other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_link_text("faculty study program").click()
        driver.find_element_by_id("facultyStudyProgram-btn").click()
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
