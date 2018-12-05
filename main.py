import numpy
from selenium import webdriver
from time import sleep
import util

#load the contacts to be sent from the csv
sendToContacts = util.filter_the_contacts("contact.csv");

#Add your path to the chromedriver where you have installed it
driver = webdriver.Chrome('C:/Users/varly/OneDrive/Desktop/PYTHON/chromedriver_win32/chromedriver.exe')
driver.get('https://web.whatsapp.com')


#This will wait for 15 seconds until you scan the qr code and start the whatsapp
sleep(15) 


contacts = dict()

for key, value in sendToContacts.items():
    greeting_msg = "Hello, *"
    content_msg = "* Merry Christmas!!  May this Christmas end the present year on a cheerful note and make way for a fresh and bright New Year. May the joy and peace of Christmas be with you all through the Year. Here’s wishing you a Merry Christmas and a Happy New Year!!"

    input_box = driver.find_element_by_css_selector("input[type='text']")
    input_box.click()
    input_box.send_keys(key)

    sleep(2)

    userbox = driver.find_element_by_css_selector("span[title='"+key+"']")
    userbox.click()

    inputbox = driver.find_element_by_css_selector("div[data-tab='1']")
    inputbox.click()

    inputbox.send_keys(greeting_msg + value + content_msg)
    
    send_button = driver.find_element_by_css_selector("span[data-icon='send']")
    send_button.click()

    sleep(2)    

