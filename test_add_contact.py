# -*- coding: utf-8 -*-
from selenium import webdriver
from contact import Contact
import unittest


class TestAddAddress(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def log_in(self, driver, username, password):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def add_address(self, driver, contact):
        driver.find_element_by_link_text("add new").click()

        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.name)
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.second_name)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.family_name)
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_homepage(self, driver):
        driver.find_element_by_link_text("home page").click()

    def log_out(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def test_case_address(self):
        driver = self.driver
        self.open_home_page(driver)
        self.log_in(driver, "admin", "secret")
        self.add_address(driver, Contact("James", "Marshall", "Hendrix", "ACME", "Some Street",
                         "8 (000) 000-00-01"))
        self.return_to_homepage(driver)
        self.log_out(driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
