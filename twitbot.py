from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        Bot = self.bot 
        Bot.get('https://twitter.com/login')
        time.sleep(3)
        email = Bot.find_element_by_class_name('email-input')
        password = Bot.find_element_by_class_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweets(self,hashtag):
        Bot = self.bot
        Bot.get('https://twitter.com/search?q='+ hashtag + '&src=typd')
        time.sleep(60)
        for i in range(0,3):
            Bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = Bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink path') for elem in tweets]
            print(links)
            for link in links:
                Bot.get('https://twitter.com'+ link)
                try:
                    Bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)


arsim = TwitterBot('arsimch9337@gmail.com','0359337')
arsim.login()
arsim.like_tweets('pakistanzindabad')


