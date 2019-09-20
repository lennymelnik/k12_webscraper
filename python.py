from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import userpass
import time
import numpy as np
import pandas as pd

driver = webdriver.Chrome("E:\Github\chromedriver")
driver.maximize_window()
course=[]
assignment=[]
due=[]
driver.get("https://login-learn.k12.com/#schedule")
driver.implicitly_wait(5)
username = driver.find_element_by_name('username')
#username = driver.find_element_by_id("input-text-username")
password = driver.find_element_by_name('password')
login = driver.find_element_by_id('c97')

username.send_keys("leonardmelnik")
password.send_keys(userpass.passWORD)
login.click()
driver.implicitly_wait(5)
driver.find_element_by_link_text('MY SCHEDULE').click()
driver.implicitly_wait(5)
#nothing = driver.find_elements_by_class_name('empty-message')
#publicSpeaking = driver.find_element_by_link_text('ENG020 Summit Public Speaking')
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
pressNext = '//*[@id="components"]/div/div[1]/div/div[1]/form/div[3]/div/span[2]'

def recursive():
 for i in range(20):
        g = True
        i = 1
        if(check_exists_by_xpath('//*[@id="components"]/div/div[2]/div/div[1]/div/div[3]/table/tbody/tr/td[1]/div/div[2]/div/div/a') == True):
            while (g == True):  # What happens per day
                tbodyXpath = '//*[@id="components"]/div/div[2]/div/div[1]/div/div[3]/table/tbody/tr[' + str(
                    i) + ']/td[1]/div/div[2]/div/div/a'
                assignmentName = '//*[@id="components"]/div/div[2]/div/div[1]/div/div[3]/table/tbody/tr[' + str(
                    i) + ']/td[2]/a'
                if (check_exists_by_xpath(tbodyXpath) == True):
                    course.append(driver.find_element_by_xpath(tbodyXpath).get_property('title'))
                    assignment.append(driver.find_element_by_xpath(assignmentName).get_property('title'))
                    dateTime = driver.find_element_by_xpath(pressNext).get_property('href')
                    due.append(dateTime)
                    print(i, course, assignment)
                    i = i + 1
                elif (check_exists_by_xpath(tbodyXpath) == False):  # if no more assignments
                    g = False
        driver.find_element_by_xpath(pressNext).click()
        time.sleep(1)
recursive()
courseArray = np.asarray(course).reshape(len(course),1)
assignmentArray = np.asarray(assignment).reshape(len(course),1)
dueArray = np.asarray(due).reshape(len(course),1)
print(courseArray,assignmentArray)

