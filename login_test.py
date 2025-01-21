from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

# Github credentials
username = os.getenv("GIT_USER")
password = os.getenv("GIT_PWD")

# initialize the Chrome driver
from selenium.webdriver.chrome.service import Service

service = Service("C:\\gbrowserdrivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# head to github login page
driver.get("https://accounts.spotify.com/en/login")
# find username/email field and send the username itself to the input field
driver.find_element("id", "login_field").send_keys(username)
# find password input field and insert password as well
driver.find_element("id", "password").send_keys(password)
# click login button
driver.find_element("name", "Log In").click()
# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=20).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")


# close the driver
driver.close()