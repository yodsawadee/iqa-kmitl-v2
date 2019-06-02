# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCase3CreateProfessor(unittest.TestCase):
    def setUp(self):
        print()
        print("test case 3-1: create professor ")
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case3_create_professor(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("thisispassword")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Study Program(หลักสูตร)___________________'])[1]/following::b[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_professor_id").click()
        driver.find_element_by_id("id_professor_id").clear()
        driver.find_element_by_id("id_professor_id").send_keys("VASUDO")
        driver.find_element_by_id("id_academic_title").click()
        driver.find_element_by_id("id_academic_title").clear()
        driver.find_element_by_id("id_academic_title").send_keys(u"ดร.")
        driver.find_element_by_id("id_name_surname").click()
        driver.find_element_by_id("id_name_surname").clear()
        driver.find_element_by_id("id_name_surname").send_keys(u"วสุ อุดมเพทายกุล")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมเกษตร]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=วิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมระบบการผลิต]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาการจัดการวิศวกรรมและเทคโนโลยี (หลักสูตรนานาชาติ)]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_professor_id").click()
        driver.find_element_by_id("id_professor_id").clear()
        driver.find_element_by_id("id_professor_id").send_keys("WIBOPO")
        driver.find_element_by_id("id_academic_title").click()
        driver.find_element_by_id("id_academic_title").clear()
        driver.find_element_by_id("id_academic_title").send_keys(u"อ.")
        driver.find_element_by_id("id_name_surname").click()
        driver.find_element_by_id("id_name_surname").clear()
        driver.find_element_by_id("id_name_surname").send_keys(u"วิบูลย์ พร้อมพานิชย์")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=วิศวกรรมศาสตรบัณฑิต สาขาวิศวกรรมวัสดุนาโน]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[4]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมดนตรีและสื่อประสม]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[5]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_responsible_program | label=หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมดนตรีและสื่อประสม]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[5]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมดนตรีและสื่อประสม]]
        driver.find_element_by_id("id_responsible_program").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาการจัดการโลจิสติกส์ (หลักสูตรนานาชาติ)]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[6]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_professor_id").click()
        driver.find_element_by_id("id_professor_id").clear()
        driver.find_element_by_id("id_professor_id").send_keys("CHAINU")
        driver.find_element_by_id("id_academic_title").click()
        driver.find_element_by_id("id_academic_title").clear()
        driver.find_element_by_id("id_academic_title").send_keys(u"ผศ.ดร.")
        driver.find_element_by_id("id_name_surname").click()
        driver.find_element_by_id("id_name_surname").clear()
        driver.find_element_by_id("id_name_surname").send_keys(u"ชัยวัฒน์ หนูทอง")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรบริหารธุรกิจบัณฑิต (หลักสูตรนานาชาติ)]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[7]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรครุศาสตร์อุตสาหกรรมบัณฑิต สาขาวิชาครุศาสตร์เกษตร]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[8]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรปรัชญาดุษฎีบัณฑิต สาขาวิชาเกษตรศาสตร์]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[9]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_professor_id").click()
        driver.find_element_by_id("id_professor_id").clear()
        driver.find_element_by_id("id_professor_id").send_keys("JANTPH")
        driver.find_element_by_id("id_academic_title").click()
        driver.find_element_by_id("id_academic_title").clear()
        driver.find_element_by_id("id_academic_title").send_keys(u"รศ.")
        driver.find_element_by_id("id_name_surname").click()
        driver.find_element_by_id("id_name_surname").clear()
        driver.find_element_by_id("id_name_surname").send_keys(u"จันทนี เพชรานนท์")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาเทคโนโลยีการหมัก]]
        driver.find_element_by_id("id_responsible_program").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรปรัชญาดุษฎีบัณฑิต สาขาวิชาเกษตรศาสตร์]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[9]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรครุศาสตร์อุตสาหกรรมบัณฑิต สาขาวิชาครุศาสตร์เกษตร]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[8]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาการจัดการโลจิสติกส์ (หลักสูตรนานาชาติ)]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[6]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรบริหารธุรกิจบัณฑิต (หลักสูตรนานาชาติ)]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[7]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรศิลปศาสตรบัณฑิต สาขาวิชานวัตกรรมการท่องเที่ยวและการบริการ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[11]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรศิลปกรรมศาสตรบัณฑิต สาขาวิชาการออกแบบสนเทศสามมิติ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[12]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_professor_id").click()
        driver.find_element_by_id("id_professor_id").clear()
        driver.find_element_by_id("id_professor_id").send_keys("NAKOSR")
        driver.find_element_by_id("id_academic_title").click()
        driver.find_element_by_id("id_academic_title").clear()
        driver.find_element_by_id("id_academic_title").send_keys(u"อ.ดร.")
        driver.find_element_by_id("id_name_surname").click()
        driver.find_element_by_id("id_name_surname").clear()
        driver.find_element_by_id("id_name_surname").send_keys(u"นคร ศรีสุขุมบวรชัย")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาเทคโนโลยีสารสนเทศ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[14]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาปิโตรเคมี (หลักสูตรนานาชาติ)]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[13]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรศิลปศาสตรบัณฑิต สาขาวิชานวัตกรรมการท่องเที่ยวและการบริการ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[11]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรศิลปกรรมศาสตรบัณฑิต สาขาวิชาการออกแบบสนเทศสามมิติ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[12]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_professor_id").click()
        driver.find_element_by_id("id_professor_id").clear()
        driver.find_element_by_id("id_professor_id").send_keys("KRITSM")
        driver.find_element_by_id("id_academic_title").click()
        driver.find_element_by_id("id_academic_title").clear()
        driver.find_element_by_id("id_academic_title").send_keys(u"ผศ.")
        driver.find_element_by_id("id_name_surname").click()
        driver.find_element_by_id("id_name_surname").clear()
        driver.find_element_by_id("id_name_surname").send_keys(u"กฤษณ์ เสมอพิทักษ์")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาเทคโนโลยีการหมัก]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[10]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรปรัชญาดุษฎีบัณฑิต สาขาวิชาเกษตรศาสตร์]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[9]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรครุศาสตร์อุตสาหกรรมบัณฑิต สาขาวิชาครุศาสตร์เกษตร]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[8]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรบริหารธุรกิจบัณฑิต (หลักสูตรนานาชาติ)]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[7]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_professor_id").click()
        driver.find_element_by_id("id_professor_id").clear()
        driver.find_element_by_id("id_professor_id").send_keys("CHUCPI")
        driver.find_element_by_id("id_academic_title").click()
        driver.find_element_by_id("id_academic_title").clear()
        driver.find_element_by_id("id_academic_title").send_keys(u"รศ.ดร.")
        driver.find_element_by_id("id_name_surname").click()
        driver.find_element_by_id("id_name_surname").clear()
        driver.find_element_by_id("id_name_surname").send_keys(u"ชูชาติ ปิณฑวิรุจน์")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมเกษตร]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=วิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมระบบการผลิต]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาการจัดการวิศวกรรมและเทคโนโลยี (หลักสูตรนานาชาติ)]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[3]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=วิศวกรรมศาสตรบัณฑิต สาขาวิศวกรรมวัสดุนาโน]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[4]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรศิลปกรรมศาสตรบัณฑิต สาขาวิชาการออกแบบสนเทศสามมิติ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[12]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรศิลปศาสตรบัณฑิต สาขาวิชานวัตกรรมการท่องเที่ยวและการบริการ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[11]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาเทคโนโลยีการหมัก]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[10]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_responsible_program | label=หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาเทคโนโลยีสารสนเทศ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::option[14]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_professor_id").click()
        driver.find_element_by_id("id_professor_id").clear()
        driver.find_element_by_id("id_professor_id").send_keys("SUPATA")
        driver.find_element_by_id("id_academic_title").click()
        driver.find_element_by_id("id_academic_title").clear()
        driver.find_element_by_id("id_academic_title").send_keys(u"ผศ.ดร.")
        driver.find_element_by_id("id_name_surname").click()
        driver.find_element_by_id("id_name_surname").clear()
        driver.find_element_by_id("id_name_surname").send_keys(u"สุพันธุ์ ตั้งจิตกุศลมั่น")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible program'])[1]/following::input[1]").click()
        driver.find_element_by_link_text("home").click()
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
