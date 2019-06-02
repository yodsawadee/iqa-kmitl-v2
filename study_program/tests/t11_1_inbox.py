# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class VTestCase11AdminInbox(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 11: admin inbox ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_v_test_case11_admin_inbox(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("thisispassword")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Assessment(การประเมินผล)___________________'])[1]/following::b[2]").click()
        driver.find_element_by_id("Inbox-btn").click()
        driver.find_element_by_id("CreateIssue-btn").click()
        driver.find_element_by_id("id_topic").click()
        driver.find_element_by_id("id_topic").clear()
        driver.find_element_by_id("id_topic").send_keys("[[ this is announcement written by ADMIN ]]")
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("content also written by ADMIN")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[2]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='[[ this is announcement written by ADMIN ]]'])[1]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='inbox'])[1]/following::h5[1]").click()
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_topic").clear()
        driver.find_element_by_id("id_topic").send_keys("[[ ADMIN is writing this topic ]]")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='content also written by ADMIN'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='admin'])[2]/following::h6[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='inbox'])[1]/following::h5[1]").click()
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("ADMIN is writing the content")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='content also written by ADMIN'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Topic'])[1]/following::h6[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='inbox'])[1]/following::h5[1]").click()
        driver.find_element_by_id("id_topic").click()
        driver.find_element_by_id("id_topic").clear()
        driver.find_element_by_id("id_topic").send_keys("[[[ ADMIN is writing this topic ]]]")
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("ADMIN is writing the content!")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='ADMIN is writing the content'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Topic'])[1]/following::a[1]").click()
        driver.find_element_by_id("issue_detail-btn").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("admin also commenting this")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::input[2]").click()
        driver.find_element_by_link_text("edit").click()
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("ADMIN also commenting this")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='admin also commenting this'])[1]/following::input[2]").click()
        driver.find_element_by_link_text("Logout").click()
    
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
