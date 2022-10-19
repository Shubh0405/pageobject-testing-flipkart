from selenium import webdriver

class Driver:

    def __init__(self, platform):

        if platform == "web":
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()

