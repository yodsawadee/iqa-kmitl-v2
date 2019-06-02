# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class YTestCase11ReplyInboxAdmin(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 11: admin reply inbox ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_y_test_case11_reply_inbox_admin(self):
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
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='[[ ENGINEER is reporting for TISSUE ]]'])[1]/following::a[1]").click()
        driver.find_element_by_id("issue_detail-btn").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("reply from admin")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::input[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='from: admin'])[3]/preceding::a[1]").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("reply from ADMIN")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='reply from admin'])[1]/following::input[2]").click()
        driver.find_element_by_link_text("edit").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("ADMIN also commenting this one.")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='ADMIN also commenting this'])[1]/following::input[2]").click()
        driver.find_element_by_link_text("inbox").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='[[ INTERNATIONAL COLLEGE report for a TISSUE ]]'])[1]/following::h6[3]").click()
        driver.find_element_by_id("issue_detail-btn").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("there is no tissue for engineer")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::input[2]").click()
        driver.find_element_by_link_text("edit").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=id_content | ]]
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("there is NO TISSUE for ENGINEER")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='there is no tissue for engineer'])[1]/following::input[2]").click()
        driver.find_element_by_link_text("inbox").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Topic'])[1]/following::h6[3]").click()
        driver.find_element_by_id("issue_detail-btn").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("the tissue is ready")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::input[2]").click()
        driver.find_element_by_link_text("edit").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("the tissue is ready for INTERNATIONAL COLLEGE")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='the tissue is ready'])[1]/following::input[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='admin'])[1]/following::nf[1]").click()
        driver.find_element_by_xpath("//div[@id='login-container']/div").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("eng")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("eng")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_id("Faculty-btn").click()
        driver.find_element_by_id("Inbox-btn").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='eng'])[2]/following::h6[1]").click()
        driver.find_element_by_id("issue_detail-btn").click()
        driver.find_element_by_id("id_content").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("nein...")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::input[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='from: eng'])[3]/preceding::a[1]").click()
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("id_content").clear()
        driver.find_element_by_id("id_content").send_keys("NEINNN!!")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='nein...'])[1]/following::input[2]").click()
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
