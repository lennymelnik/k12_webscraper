from selenium import webdriver, WebElement
from selenium import web
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products=[]
prices=[]
ratings=[]
driver.get("https://login-learn.k12.com/#login")

WebElement username = driver.find_element_by_id("input-text-username")
WebElement password = driver.find_element_by_id("input-password-password")
WebElement login = driver.find_element_by_id("c163")
username.send_keys("leonardmelnik")
password.send_keys("testing123")
login.click()


