from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set the path to your ChromeDriver executable
serv_obj=Service("C:\\Users\\Amani\\Desktop\\New folder\\chromedriver.exe")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=serv_obj)

# Maximize the browser window
driver.maximize_window()

#time delay
time.sleep(2)

# Navigate to the given URL
driver.get('https://www.saucedemo.com/')

# Find the username and password fields and login
username = driver.find_element(By.ID,'user-name').send_keys('standard_user')
password = driver.find_element(By.ID,'password').send_keys('secret_sauce')

#time delay
time.sleep(2)

login_button = driver.find_element(By.ID, 'login-button').click()

# Get the title of the webpage
title = driver.title
print(f'Title of the webpage: {title}')

# Get the current URL of the webpage
current_url = driver.current_url
print(f'Current URL of the webpage: {current_url}')

#Extract the entire contents of the webpage and save it to a text file
webpage_content = driver.page_source

with open('webpage_task_11.txt', 'w') as file:
    file.write(webpage_content)

#time delay
time.sleep(3)

# Close the browser window
driver.close()