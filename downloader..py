from selenium import webdriver
import urllib.request
import string
import random
from time import  sleep
import wget


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
     return ''.join(random.choice(chars) for _ in range(size))

def getpic():
    
    rand=id_generator()
    postfix="c.png"
    imgname=rand+postfix
    driver = webdriver.Chrome()
    driver.get('https://edu.uk.ac.ir/home/balancer/captcha.aspx')
    images = driver.find_elements_by_tag_name('img')
    for image in images:
        src=image.get_attribute('src')
        wget.download(src, imgname)


    driver.close()

for i in range(0,100):
    getpic()
    #sleep(5)