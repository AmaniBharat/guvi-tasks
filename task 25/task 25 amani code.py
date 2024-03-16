from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
###############launching the browser by using the driver variable##############
chrome_service = ChromeService("C:\\Users\\Amani\\Desktop\\New folder\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
actions=ActionChains(driver)
############launching the url in the browser#########
driver.get("https://www.imdb.com/search/name/")
time.sleep(10)
driver.maximize_window()
############handling the errors by using the exceptions concepts########
wait = WebDriverWait(driver, 15, ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementNotInteractableException,
                                                     TimeoutException])
#####filling the name details######
for _ in range(8):
    actions.send_keys(Keys.DOWN).perform()
name_click=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='nameTextAccordion']/div[1]/label/span[1]")))
name_click.click()
name_text= wait.until(EC.presence_of_element_located((By.NAME, 'name-text-input')))
name_text.send_keys("amani")
######filling the birthdate details####
for _ in range(15):
    actions.send_keys((Keys.DOWN)).perform()
birth_click=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='birthDateAccordion']/div[1]/label/span[1]/div")))
birth_click.click()
birth_startdate=wait.until(EC.presence_of_element_located((By.NAME,"birth-date-start-input")))
birth_startdate.send_keys("29-10-2021")
birth_enddate=wait.until(EC.presence_of_element_located((By.NAME,"birth-date-end-input")))
birth_enddate.send_keys("30-10-2022")
######## birthday details ###############
for _ in range(10):
    actions.send_keys(Keys.DOWN).perform()
birthday_click=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='birthdayAccordion']/div[1]/label/span[1]/div")))
birthday_click.click()
birthday_data=wait.until(EC.presence_of_element_located((By.NAME,"birthday-input")))
birthday_data.send_keys("29-10-2021")
###########awards_details############
for _ in range(15):
    actions.send_keys(Keys.DOWN).perform()
awards_click=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='awardsAccordion']/div[1]/label")))
awards_click.click()
actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.ENTER).perform()
########## page topics ######################
for _ in range(10):
    actions.send_keys(Keys.DOWN).perform()
page_topics=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='pageTopicsAccordion']/div[1]/label")))
page_topics.click()
actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.ENTER).perform()
##########death date details#############
for _ in range(10):
    actions.send_keys(Keys.DOWN).perform()
death_click=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='deathDateAccordion']/div[1]/label/span[1]/div")))
death_click.click()
death_start=wait.until(EC.presence_of_element_located((By.NAME,"death-date-start-input")))
death_start.send_keys("31-10-2020")
death_end=wait.until(EC.presence_of_element_located((By.NAME,"death-date-end-input")))
death_end.send_keys("31-10-2020")
###########gender identity#################
for _ in range(5):
    actions.send_keys(Keys.DOWN).perform()
gender_click=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='genderIdentityAccordion']/div[1]/label/span[1]/div")))
gender_click.click()
gender_select=wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Female']")))
actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.ENTER).perform()
#############credits details#########
for _ in range(5):
    actions.send_keys(Keys.DOWN).perform()
credits=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='filmographyAccordion']/div[1]/label")))
credits.click()
credit_data=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='accordion-item-filmographyAccordion']/div/div/div/div[1]/input")))
#credit_data.send_keys("0")
#############Adult Names#######
for _ in range(20):
    actions.send_keys(Keys.DOWN).perform()
adult_name =wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="adultNamesAccordion"]/div[1]/label/span[1]/div')))
adult_name.click()
select_radio = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="include-adult-names"]')))
select_radio.click()
########## see results tab#############
for _ in range(3):
    actions.send_keys(Keys.PAGE_UP).perform()
see_click=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button[2]/span')))
see_click.click()
time.sleep(5)