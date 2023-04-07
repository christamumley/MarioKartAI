#https://mkpc.malahieude.net/mariokart.php
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import keyboard
import time

import os

from SegmentationAI import Decider

class Driver:

    def __init__(self, url="https://mkpc.malahieude.net/mariokart.php"):
        self.link = url
        self.driver = webdriver.Firefox()
        self.driver.get(url)

        self.decider = Decider()

        if not os.path.isdir("Images"):
            # So that we can start capturing the screen
            os.mkdir("Images")

    def run(self, debug_mode=False):
        # Select Grand Prix
        elem = self.driver.find_element(By.XPATH, '//input[@value="Grand Prix"]')
        elem.click()
        # Select player (mario)
        elem = self.driver.find_element(By.XPATH, '//div[@id="perso-selector-mario"]')
        elem.click()

        #Select map
        elem = self.driver.find_element(By.XPATH, '//img[@src="images/cups/champi.gif"]')
        elem.click()

        # Sleep as you cannot move for 3 seconds at the start
        time.sleep(2.8)


        # Race now starts - Do something?
        iter = 0
        while True:
            iter += 1

            if debug_mode:
                self.capture_screen(iter)
            else:
                self.decide_movement()

    def decide_movement(self, img_path="Images/current_state.png"):
        ActionChains(self.driver).key_down("P").perform()
        self.driver.save_screenshot(img_path)
        action, move = self.decider.direction_to_move(img_path)
        ActionChains(self.driver).key_up("P").perform()
        print(f"We should turn {move}")
        ActionChains(self.driver).key_up(Keys.LEFT).key_up(Keys.UP).key_up(Keys.LEFT).perform()
        if move != 'straight':
            # ActionChains(self.driver).key_up(Keys.LEFT).key_up(Keys.UP).key_up(Keys.LEFT).perform()
            ActionChains(self.driver).key_down(action).key_down(Keys.UP).perform()
            time.sleep(0.1)
            ActionChains(self.driver).key_up(action).perform()
            time.sleep(0.05)
            # ActionChains(self.driver).key_down(Keys.UP).perform()
        else:
            ActionChains(self.driver).key_down(action).perform()
            time.sleep(0.1)
        # time.sleep(0.1)
        # ActionChains(self.driver).key_up(Keys.LEFT).key_up(Keys.UP).key_up(Keys.LEFT).perform()

        # ActionChains(self.driver).key_up(Keys.LEFT).key_up(Keys.UP).key_up(Keys.RIGHT).perform()
        # ActionChains(self.driver).key_up(Keys.LEFT).key_up(Keys.RIGHT).perform()

        # time.sleep(0.01)
        # ActionChains(self.driver).key_down(Keys.UP).perform()
        # # time.sleep(0.)

    def capture_screen(self, iter):
        actions = ActionChains(self.driver).key_down(Keys.UP)
        actions.perform()
        self.driver.save_screenshot(f"Images/captured2_{iter}.png")
        time.sleep(0.5)
    def capture_keyboard_acts(self, iter):
        """
        Used to capture training images - just drives straight
        :return:
        """
        up = keyboard.is_pressed('up')
        left = keyboard.is_pressed('left')
        right = keyboard.is_pressed('right')

        print(f"up: {up} left: {left} right: {right}")

        img_path = f"ReinforcementImages/reinforce3-{iter}_"
        if up:
            img_path += "up_"
        if left:
            img_path += "left_"
        if right:
            img_path += "right_"

        img_path += ".png"

        self.driver.save_screenshot(img_path)
        # actions = ActionChains(self.driver).key_down(Keys.UP)
        # actions.perform()
        # self.driver.save_screenshot(f"Images/captured2_{iter}.png")
        # time.sleep(0.5)



if __name__ == "__main__":
    Driver().run(debug_mode=False)


"""
    Robert Mode: 
       # Robert Mode 
        # img_src = "https://cdn.discordapp.com/attachments/1067893021259087905/1088842575768727582/image.png"
        #
        # imgE = self.driver.find_element(By.XPATH, '//img[@src="images/sprites/sprite_mario.png"]')
        # elems = self.driver.find_elements(By.XPATH, '//div[@class="pixelated"]/img')
        # for imgE in elems:
        #     self.driver.execute_script("arguments[0].src='" + img_src + "'", imgE);

        # self.driver.execute_script("arguments[0].src='" + img_src + "'", imgE);

"""