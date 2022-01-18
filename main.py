from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 30
PROMISED_UP = 30
CHROME_DRIVER_PATH = os.environ.get("DRIVER_PATH")
TWITTER_EMAIL = os.environ.get("EMAIL")
TWITTER_PASSWORD = os.environ.get("PASSWORD")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        ser = Service(driver_path)
        self.driver = webdriver.Chrome(service=ser)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        print("get Internet speed")
        self.driver.get("https://www.speedtest.net/")
        start_test = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        start_test.click()
        time.sleep(60)
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")

        self.down = float(download_speed.text)
        self.up = float(upload_speed.text)

        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        print("tweet at provider")
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in.click()
        time.sleep(2)
        email_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        email_field.send_keys(TWITTER_EMAIL)
        email_field.send_keys(Keys.ENTER)
        time.sleep(2)
        phone_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        phone_field.send_keys(PHONE_NUMBER)
        phone_field.send_keys(Keys.ENTER)
        time.sleep(2)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)
        time.sleep(2)

        tweet_text = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_text.send_keys("Hey Internet Provider, why is my internet speed"
                             f"{self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up")

        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet.click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()

if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider()

