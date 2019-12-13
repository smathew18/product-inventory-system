import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPISSuppliersAdmin(unittest.TestCase):

    def setUp(self) :
        self.driver = webdriver.Chrome()

    def test_pis(self):

        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://pis-assignment4.herokuapp.com/admin/login/?next=/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

        driver.get("https://pis-assignment4.herokuapp.com/admin/pis/")
        time.sleep(1)
        #Click on Suppliers tab

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/table/tbody/tr[4]/th/a")
        elem.click()
        time.sleep(1)

        # Clicks on add supplier button
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
        time.sleep(2)

        # fill the supplier details
        elem = driver.find_element_by_id("id_user")
        elem.send_keys("instructor")
        elem = driver.find_element_by_id("id_suppliername")
        elem.send_keys("Infoway Group")
        elem = driver.find_element_by_id("id_supplieraddress")
        elem.send_keys("4800 Dodge Street")
        elem = driver.find_element_by_id("id_suppliercity")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_id("id_supplierstate")
        elem.send_keys("Nebraska")
        elem = driver.find_element_by_id("id_supplierzipcode")
        elem.send_keys("68152")
        time.sleep(2)


        # xpath, clicks on save button for add supplier

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(5)

        # xpath, clicks on suppliers to edit
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[3]/th/a").click()
        time.sleep(2)

        # Edit supplier details
        elem = driver.find_element_by_id("id_supplieraddress")
        elem.clear()
        elem.send_keys("8807 Q Street")
        elem = driver.find_element_by_id("id_supplierzipcode")
        elem.clear()
        elem.send_keys("68127")
        time.sleep(1)

        # xpath, clicks on save button for edit supplier
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
