#https://mkpc.malahieude.net/mariokart.php
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
# import keyboard
import time
import threading

from pynput import keyboard
import pandas as pd
import time


import os
import numpy as np


class keylistener:
    def __init__(self, driver):
        self.left = None
        self.right = None
        self.up = None

        self.driver = driver
        self.iter = 0
        self.rows = []

        self.csv_path = "image_mappings.csv"
    def on_press(self, key):
        if key == keyboard.Key.up:
            self.up = time.time()
        elif key == keyboard.Key.left:
            self.left = time.time()
        elif key == keyboard.Key.right:
            self.right = time.time()


    def on_release(self, key):
        up_time, left_time, right_time = 0, 0, 0
        if key == keyboard.Key.up:
            up_time = time.time() - self.up
        elif key == keyboard.Key.left:
            left_time = time.time() - self.left
        elif key == keyboard.Key.right:
            right_time = time.time() - self.right
        f_path = f"ReinforcementImages/reinforce1-{self.iter}.png"
        self.rows.append({'name':f_path, 'left':left_time, 'right':right_time, 'up':up_time})
        self.driver.save_screenshot(f_path)
        df = pd.DataFrame(self.rows)

        df.to_csv(self.csv_path)
    def listen(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

class Crawler:
    def __init__(self, url="https://mkpc.malahieude.net/mariokart.php"):
        self.link = url

        self.driver = webdriver.Firefox()
        self.driver.get(url)
    def run(self, debug_mode=False):
        keyClient = keylistener(self.driver)

        threading.Thread(target=keyClient.listen).start()

        # Select Grand Prix
        elem = self.driver.find_element(By.XPATH, '//input[@value="Time trial"]')
        elem.click()
        # Select player (mario)
        elem = self.driver.find_element(By.XPATH, '//div[@id="perso-selector-mario"]')
        elem.click()

        # Select map
        elem = self.driver.find_element(By.XPATH, '//img[@src="images/cups/champi.gif"]')
        elem.click()
        # elem = self.driver.find_element(By.XPATH, '//img[@src="images/cups/champi.gif"]')
        elem = self.driver.find_element(By.XPATH, '//img[@src="images/selectors/select_map1.png"]')
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element(By.XPATH, '//input[@value="Play alone"]')
        elem.click()

        # Sleep as you cannot move for 3 seconds at the start
        time.sleep(2.8)

        iter = 0
        while True:
            iter += 1
            time.sleep(1)
            # self.capture_keyboard_acts()


if __name__ == "__main__":
    Crawler().run()


