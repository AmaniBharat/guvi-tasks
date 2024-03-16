from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set the path to your ChromeDriver executable
serv_obj=Service("C:\\Users\\Amani\\Desktop\\New folder\\chromedriver.exe")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=serv_obj)

# Maximize the browser window
driver.maximize_window()

# Open the URL
driver.get('https://www.saucedemo.com/')

# Display cookies before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:", cookies_before_login)

# Find the username, password, and login button elements
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

#time delay
time.sleep(2)

# Display cookies after login
cookies_after_login = driver.get_cookies()
print("Cookies after login:", cookies_after_login)

#time delay
time.sleep(1)

# For demonstration purposes, clicking on the inventory item
driver.find_element(By.ID,"react-burger-menu-btn").click()

time.sleep(2)

# Perform logout
driver.find_element(By.ID,"logout_sidebar_link").click()

# Display cookies after logout
cookies_after_logout = driver.get_cookies()
print("Cookies after logout:", cookies_after_logout)

#time delay
time.sleep(3)

# Close the browser
driver.close()