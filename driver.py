#https://mkpc.malahieude.net/mariokart.php
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

import os


class Driver:

    def __init__(self, url="https://mkpc.malahieude.net/mariokart.php"):
        self.link = url
        self.driver = webdriver.Firefox()
        self.driver.get(url)

        if not os.path.isdir("Images"):
            # So that we can start capturing the screen
            os.mkdir("Images")

    def run(self):
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

        # js.executeScript("document.getElementById('//id of element').setAttribute('attr', '10')");

        # Robert Mode
        # img_src = "https://cdn.discordapp.com/attachments/1067893021259087905/1088842575768727582/image.png"
        #
        # imgE = self.driver.find_element(By.XPATH, '//img[@src="images/sprites/sprite_mario.png"]')
        # elems = self.driver.find_elements(By.XPATH, '//div[@class="pixelated"]/img')
        # for imgE in elems:
        #     self.driver.execute_script("arguments[0].src='" + img_src + "'", imgE);

        # self.driver.execute_script("arguments[0].src='" + img_src + "'", imgE);

        # Race now starts - Do something?
        iter = 0
        while True:
            iter += 1
            # Just go forward forever right now
            actions = ActionChains(self.driver).key_down(Keys.UP)
            actions.perform()

            self.driver.save_screenshot(f"Images/captured2_{iter}.png")
            time.sleep(0.5)



if __name__ == "__main__":
    Driver().run()