from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 30
PROMISED_UP = 30
CHROME_DRIVER_PATH = "/home/janf/Development/chromedriver"
TWITTER_EMAIL = "janf.tst@gmail.com"
TWITTER_PASSWORD = "T3$71n9U$3r"


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



bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
# bot.tweet_at_provider()

