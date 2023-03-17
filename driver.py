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

    """
        
        
    """

    def run(self):
        # Select Grand Prix
        elem = self.driver.find_element(By.XPATH, '//input[@value="Grand Prix"]')
        elem.click()
        # Select player (mario)
        elem = self.driver.find_element(By.XPATH, '//div[@id="perso-selector-mario"]')
        elem.click()

        #Select cup
        elem = self.driver.find_element(By.XPATH, '//img[@src="images/cups/champi.gif"]')
        elem.click()

        # Sleep for 3 seconds to try to beat the 3 second countdown / prevent AI from trying to drive while
        # it cant
        time.sleep(3)
        # Race now starts - Do something?
        iter = 0
        while True:
            iter += 1
            # Just go forward forever right now
            actions = ActionChains(self.driver).key_down(Keys.UP)
            actions.perform()

            self.driver.save_screenshot(f"Images/captured_{iter}.png")
            time.sleep(0.2)
        # self.driver.close()

if __name__ == "__main__":
    Driver().run()