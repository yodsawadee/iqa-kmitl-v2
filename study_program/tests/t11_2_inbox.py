# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class WTestCase11EngineerInbox(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 11: engineer inbox ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_w_test_case11_engineer_inbox(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("eng")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("eng")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Assessment(การประเมินผล)___________________'])[1]/following::b[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='AssessmentCalendar(ปฏิทินการประเมิน)___________________'])[1]/following::b[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='[[[ ADMIN is writing this topic ]]]'])[1]/following::div[1]").click()
        driver.find_element_by_id("issue_detail-btn").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("I see")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::input[2]").click()
        driver.find_element_by_link_text("edit").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_xpath("//body").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //body | ]]
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("ENGINEER see")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='I see'])[1]/following::input[2]").click()
        driver.find_element_by_link_text("inbox").click()
        driver.find_element_by_id("CreateIssue-btn").click()
        driver.find_element_by_id("id_topic").click()
        driver.find_element_by_id("id_topic").clear()
        driver.find_element_by_id("id_topic").send_keys("[[ I report for TISSUE ]]")
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("there is no tissue in faculty")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[2]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='eng'])[2]/following::h6[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='inbox'])[1]/following::h5[1]").click()
        driver.find_element_by_id("id_topic").click()
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_id("id_topic").clear()
        driver.find_element_by_id("id_topic").send_keys("[[ ENGINEER is reporting for TISSUE ]]")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='there is no tissue in faculty'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='eng'])[2]/following::h6[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='inbox'])[1]/following::h5[1]").click()
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("there is no tissue in ENGINEER faculty")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='there is no tissue in faculty'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='eng'])[2]/following::h6[1]").click()
        driver.find_element_by_id("issue_detail-btn").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("engineer is writing this")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::input[2]").click()
        driver.find_element_by_link_text("edit").click()
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("ENGINEER is writing this")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='engineer is writing this'])[1]/following::input[2]").click()
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
