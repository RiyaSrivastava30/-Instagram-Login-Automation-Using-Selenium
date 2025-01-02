#importing Libraries 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Setting web driver interact with browser 
chrome_driver_path = "F:\Machine Learning\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#Link on which we want to work
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)
USERNAME = "desi_brahaman_pr"
PASSWORD = "abc123455463463445"

#Ways to select elements
username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
#username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys(USERNAME)
password.send_keys(PASSWORD)

time.sleep(2)
password.send_keys(Keys.ENTER)


