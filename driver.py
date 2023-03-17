#https://mkpc.malahieude.net/mariokart.php
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % "1920,1080")
# chrome_options.binary_location = "chromedriver"
class Driver:

    def __init__(self, url="https://mkpc.malahieude.net/mariokart.php"):
        self.link = url
        self.driver = webdriver.Firefox()
        self.driver.get(url)

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

        # Race now starts - Do something?
        for i in range(100):
            # Just go forward forever right now
            actions = ActionChains(self.driver).key_down(Keys.UP)
            actions.perform()

            self.driver.save_screenshot(f"Images/img{i}.png")

        print(elem)


if __name__ == "__main__":
    Driver().run()