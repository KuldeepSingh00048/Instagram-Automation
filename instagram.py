from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

bot = webdriver.Edge(executable_path='C:/Users/THE KULDEEP SINGH/Desktop/instagram '
                                     'project/edge driver/msedgedriver.exe')


def login():
    bot.get('https://instagram.com/accounts/login')
    time.sleep(3)
    bot.find_element_by_name('username').send_keys("vaidehi_2908")
    bot.find_element_by_name('password').send_keys("Ajay2908" + Keys.RETURN)
    time.sleep(4)
    notNow = bot.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    notNow.click()
    time.sleep(4)
    noti = bot.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
    noti.click()
    time.sleep(4)


def like_comment():
    bot.find_element_by_class_name('_9AhH0').click()
    time.sleep(1)
    bot.find_element_by_class_name('fr66n').click()
    time.sleep(2)
    comment = bot.find_element_by_class_name("Ypffh")
    comment.click()
    comment.send_keys('Nice')
    comment.submit()
    time.sleep(2)


def follow(amount):
    i = 1
    while i <= amount:
        time.sleep(1)
        bot.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div["
                                  "1]/div[3]/button/div").click()
        bot.refresh()
        i += 1


login()
follow(1)
like_comment()
