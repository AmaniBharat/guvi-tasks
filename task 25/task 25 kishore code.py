from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# Set the path to your ChromeDriver
serv_obj=Service("C:\\Users\\Amani\\Desktop\\New folder\\chromedriver.exe")

# Create a new instance of the Chrome driver
driver: WebDriver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
act=ActionChains(driver)

# Maximize the browser window
driver.maximize_window()
# Navigate to the given URL
driver.get('https://www.imdb.com/search/name/')

driver.implicitly_wait(20)

# NAME
driver.find_element(By.XPATH,'//*[@id="nameTextAccordion"]/div[1]/label/span[1]/div').click()
driver.find_element(By.NAME,'name-text-input').send_keys('Heath Ledger')
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
wait = WebDriverWait(driver, 4)

# BIRTHDATE
driver.find_element(By.XPATH,'//*[@id="birthDateAccordion"]/div[1]/label').click()
driver.find_element(By.NAME,'birth-date-start-input').send_keys('04/04/1979')
driver.implicitly_wait(5)
driver.find_element(By.NAME,'birth-date-end-input').send_keys('04/04/1979')
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
wait = WebDriverWait(driver, 4)

# BIRTHDAY
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="birthdayAccordion"]/div[1]/label').click()
driver.find_element(By.NAME,'birthday-input').send_keys('04-04')
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
wait = WebDriverWait(driver, 4)

# AWARDS & RECOGNITION
driver.implicitly_wait(15)
driver.find_element(By.XPATH,'//*[@id="awardsAccordion"]/div[1]/label').click()
driver.find_element(By.XPATH,'//*[@id="accordion-item-awardsAccordion"]/div/section/button[2]').click()  # Best Actor-Nominated
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="accordion-item-awardsAccordion"]/div/section/button[14]').click() # Oscar-Winning
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
wait = WebDriverWait(driver, 4)

# PAGE TOPIC
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="pageTopicsAccordion"]/div[1]/label').click()
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
driver.find_element(By.XPATH,'//*[@id="accordion-item-pageTopicsAccordion"]/div/div/section/button[1]').click()  # Award Nominations
driver.find_element(By.XPATH,'//*[@id="accordion-item-pageTopicsAccordion"]/div/div/section/button[2]').click()  # Biography
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
wait = WebDriverWait(driver, 4)

# DROP DOWN
driver.implicitly_wait(5)
try:
    DD1_list=driver.find_element(By.XPATH,'//*[@id="within-topic-dropdown-id"]').click()
    if DD1_list is not None:
        for DD1 in DD1_list:
            if DD1.text == "Biography":
                DD1.click()
                break
except Exception as e:
    print("Biography not selected", e)

driver.find_element(By.NAME,'within-topic-input').send_keys("Movies")
act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.ENTER).perform()

# DEATH DATE
act.send_keys(Keys.TAB).perform()
WebDriverWait = WebDriverWait
act.send_keys('01/22/2008').perform()
act.send_keys(Keys.TAB).send_keys('01/22/2008').perform()
act.send_keys(Keys.ENTER).perform()
wait = WebDriverWait(driver, 4)

# GENDER IDENTITY
driver.find_element(By.XPATH,'//*[@id="genderIdentityAccordion"]/div[1]/label').click()
driver.find_element(By.XPATH,'//*[@id="accordion-item-genderIdentityAccordion"]/div/section/button[1]').click()
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
wait = WebDriverWait(driver, 4)

# CREDITS
driver.find_element(By.XPATH,'//*[@id="filmographyAccordion"]/div[1]/label').click()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH,'//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input').send_keys('I Am Heath Ledger')
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
Wait = WebDriverWait(driver, 10)
act.send_keys(Keys.DOWN).perform()
act.send_keys(Keys.ENTER).perform()

# ADULT NAME
driver.find_element(By.XPATH,'//*[@id="adultNamesAccordion"]/div[1]/label').click()
driver.find_element(By.ID,'include-adult-names').click()
act.send_keys(Keys.ENTER).perform()

# 2 times PAGE_UP for SEARCH.
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_UP,Keys.PAGE_UP)

# SEARCH BUTTON
driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button[2]').click()

# Collapse all  #Dorp and Down.
close=driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button')
act.double_click(close)

# Heath Ledger
driver.find_element(By.LINK_TEXT,'1. Heath Ledger').click()  # BATMAN VILLAN
driver.implicitly_wait(20)

# Close the browser
driver.close()