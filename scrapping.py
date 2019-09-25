
from selenium import webdriver
import pandas as pd
import os
import time

url = "http://turbulence.pha.jhu.edu/webquery/query.aspx"

# create a new Firefox session

chromedriver = r"C:\Users\SUNIL\Downloads\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(url)

selectElem = driver.find_element_by_xpath("//select[@name='dataset']/option[text()='transition_bl']").click()
selectElem = driver.find_element_by_xpath('//*[@id="GetVelocityAndPressure"]').click()


for i in range(175, 180, 5):
    selectElem=driver.find_element_by_xpath('//*[@id="time"]')
    time.sleep(1)
    selectElem.click()
    selectElem.clear()
    selectElem.send_keys(i)
    selectElem = driver.find_element_by_xpath('//*[@id="fileup1"]')
    selectElem.send_keys(r"C:\Users\SUNIL\Downloads\dns_falt_plate.txt")
    selectElem = driver.find_element_by_xpath('//*[@id="Button1"]').click()
    selectElem = driver.find_element_by_xpath('//*[@id="outputformat"]/tbody/tr[3]/td/label').click()
    selectElem = driver.find_element_by_xpath('//*[@id="bulkwork"]').click()
