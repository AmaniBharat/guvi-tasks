from Utilities.xlutility import Amani_excel_functions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_data import dataexcel
import pytest
import time


 ##Constants for Excel file path and sheet name
EXCEL_FILE_PATH = "C:\\Users\\Amani\\PycharmProjects\\datadriven project(excel file)\\Excel files\\new excel.xlsx"
EXCEL_SHEET_NAME = 'Sheet1'

class Test_Guvi_login:

    url = "https://www.zenclass.in/login"
    # Booting Method for running the Python Project1
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()


    def test_login(self,booting_function):

       self.driver.get(self.url)

       rows = Amani_excel_functions(EXCEL_FILE_PATH,EXCEL_SHEET_NAME).Row_Count()

       for row in range(2, rows + 1):
            username = Amani_excel_functions(EXCEL_FILE_PATH, EXCEL_SHEET_NAME).Read_Data(row, 6)
            password = Amani_excel_functions(EXCEL_FILE_PATH, EXCEL_SHEET_NAME).Read_Data(row, 7)

            username_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, dataexcel.TestSelectors.user_xpath)))
            username_input.click()
            username_input.send_keys(username)

            password_input=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                           dataexcel.TestSelectors.password_xpath)))
            password_input.click()
            password_input.send_keys(password)

            login_click=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        dataexcel.TestSelectors.login_xpath)))
            login_click.click()
            time.sleep(10)

            try:
                WebDriverWait(self.driver,10).until(EC.url_matches("https://www.zenclass.in/class"))
                Amani_excel_functions(EXCEL_FILE_PATH, EXCEL_SHEET_NAME).Write_Data(row, 8, "TEST PASS")
                profile_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                               dataexcel.TestSelectors.profile_xpath)))
                profile_click.click()
                logout_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                               dataexcel.TestSelectors.logout_xpath)))
                logout_click.click()


            except TimeoutException:

                print("login failure")
                Amani_excel_functions(EXCEL_FILE_PATH, EXCEL_SHEET_NAME).Write_Data(row, 8, "Test Failure")
                self.driver.refresh()





























