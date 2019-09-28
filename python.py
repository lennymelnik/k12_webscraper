from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time
import numpy as np
import requests
import keys

url = "https://api.trello.com/1/cards"
driver = webdriver.Chrome("E:/Github/chromedriver.exe")

driver.maximize_window()

full = []

driver.get("https://login-learn.k12.com/#schedule")

driver.implicitly_wait(5)

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
login = driver.find_element_by_id('c97')

username.send_keys(keys.username)
password.send_keys(keys.password)
login.click()

driver.implicitly_wait(5)
driver.find_element_by_link_text('MY SCHEDULE').click()
driver.implicitly_wait(5)

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

                #Defining Paths BEFORE GRABBING DATA
                tbodyXpath = '//*[@id="components"]/div/div[2]/div/div[1]/div/div[3]/table/tbody/tr[' + str(
                    i) + ']/td[1]/div/div[2]/div/div/a'
                assignmentName = '//*[@id="components"]/div/div[2]/div/div[1]/div/div[3]/table/tbody/tr[' + str(
                    i) + ']/td[2]/a'
                DueTime = '/html/body/div/section/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[3]/table/tbody/tr[' + str(
                    i) + ']/td[3]/div/div/span'
                DueDate = '/html/body/div/section/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[1]/div/div[1]/form/div[2]/div/p'
                if (check_exists_by_xpath(tbodyXpath) == True):

                    courseCurrent = driver.find_element_by_xpath(tbodyXpath).get_property('title')
                    assignmentCurrent = driver.find_element_by_xpath(assignmentName).get_property('title').replace(',','')
                    assignmentDueTime = driver.find_element_by_xpath(DueTime).text
                    #Clean up time due since sometimes text is included
                    if "Due " in assignmentDueTime:
                        assignmentDueTime = assignmentDueTime.replace('Due ','')

                    assignmentDueDate = driver.find_element_by_xpath(DueDate).text
                    assignmentDueDate = str(datetime.strptime(assignmentDueDate, '%B %d, %Y'))[0:10]

                    #Trello API
                    querystring = {"name": assignmentName, "desc": courseCurrent, "pos": "bottom","due":assignmentDueDate,
                                   "idList": keys.listId, "keepFromSource": "all", "key": keys.apiKey,
                                   "token": keys.tokenKey}
                    #Push info to api
                    response = requests.request("POST", url, params=querystring)

                    print(response.text)

                    full.append([courseCurrent, assignmentCurrent,assignmentDueDate,assignmentDueTime])


                    dateTime = driver.find_element_by_xpath(pressNext).get_property('href')
                    due.append(dateTime)

                    i = i + 1
                elif (check_exists_by_xpath(tbodyXpath) == False):  # if no more assignments
                    g = False
        driver.find_element_by_xpath(pressNext).click()
        time.sleep(1)
recursive()

#Save to csv for chrome export
np.savetxt('out.csv', (np.array(full)), delimiter=",", fmt = '%s',header='Description,Subject,Start Date, End Time')
