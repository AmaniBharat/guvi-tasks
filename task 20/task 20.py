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

# Navigate to the Cowin website
driver.get("https://www.cowin.gov.in/")

# Click on "FAQ" link to open a new window
driver.find_element(By.LINK_TEXT, "FAQ").click()

#time delay
time.sleep(2)

# Click on "Partners" link to open another new window
driver.find_element(By.XPATH, "//*[@id='navbar']/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a").click()

#time delay
time.sleep(2)

# Get the handles of all open windows
window_handles = driver.window_handles

# Display window/frame IDs in the console
for handle in window_handles:
   driver.switch_to.window(handle)
   print(f"Window/Frame ID: {handle}")
# Close the two new windows and switch back to the original window
for handle in window_handles[1:]:
    driver.switch_to.window(handle)
    driver.close()
# Switch back to the original window
driver.switch_to.window(window_handles[0])

# Perform any additional actions on the original window if needed
#time delay
time.sleep(3)

# Close the original window
driver.close()

#############################  THE PAGE OF  "https://labour.gov.in/" #######################################


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
import time

# Set the path to your ChromeDriver executable
serv_obj=Service("C:\\Users\\Amani\\Desktop\\New folder\\chromedriver.exe")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=serv_obj)

# Maximize the browser window
driver.maximize_window()

# ActionChains
actions = ActionChains(driver)

# Navigate to the Labour Ministry website
driver.get("https://labour.gov.in/")

driver.implicitly_wait(60)

#CLOSE THE Ad BANNER:
driver.find_element(By.CLASS_NAME, "open_button").click()

# Download the monthly progress report, find and click it
time.sleep(2)
element_to_hover_over = driver.find_element(By.XPATH, '//*[@id="nav"]/li[7]/a')  # DOCUMENT XPATH
time.sleep(2)
actions.move_to_element(element_to_hover_over)
time.sleep(2)
actions.perform()
driver.find_element(By.LINK_TEXT, "Monthly Progress Report").click()

time.sleep(2)
pdf=(driver.find_element(By.XPATH, '//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').click()) # PDF OF Download(227.11 KB)

time.sleep(4)
alert=driver.switch_to.alert
alert.accept()

driver.implicitly_wait(20)

#time delay
time.sleep(6)

# Get the handles of all open windows
window_handles = driver.window_handles
# Display window/frame IDs in the console
for handle in window_handles:
    driver.switch_to.window(handle)
# Close the two new windows and switch back to the original window
for handle in window_handles[1:]:
    driver.switch_to.window(handle)
    driver.close()

# Switch back to the original window
driver.switch_to.window(window_handles[0])

#time delay
time.sleep(6)

# Download 10 photos from the "Photos Gallery" under the "Media" menu
driver.find_element(By.LINK_TEXT, "Media").click()

# time delay
time.sleep(10)

driver.implicitly_wait(20)

# MANUALLY ENTER THE swachhata-hi-seva PAGE. (CON'T OPERATED THE ELEMENT)
driver.get('https://labour.gov.in/gallery/swachhata-hi-seva')

# Wait for the photos to load
photos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="quicktabs-tabpage-album_gallery-0"]/div/div[2]/div/ul/li[1]/div[1]/div/a/img'))) #Photo Gallery

# Create a folder to store downloaded photos
folder_path = 'downloaded_photos'
os.makedirs(folder_path, exist_ok=True)

# Download the first 10 photos
for i, photo in enumerate(photos[:10]):
    photo_url = photo.get_attribute('src')                          ##################   ( HERE THERE IS NO src IMAGE IN ONE LINK TAG ) ,( HAVE ONLY ONE SRC IN ONE X-PATH )
    response = requests.get(photo_url)                                                                      ###(THE CODE FOR DOWNLOAD 10 PHOTOS)
    with open(os.path.join(folder_path, f'photo_{i+1}.jpg'), 'wb') as f:
        f.write(response.content)

#time delay
time.sleep(3)

# Close the browser
driver.close()