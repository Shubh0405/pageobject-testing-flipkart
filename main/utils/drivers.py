from selenium import webdriver as selenium_driver
from appium import webdriver as appium_driver
from selenium.webdriver.chrome.options import Options

class Driver:

    def __init__(self, platform):

        if platform == "web":

            options = Options()
            options.page_load_strategy = 'eager'


            self.driver = selenium_driver.Chrome(options=options)
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
        
        if platform == "android":
            desired_cap = {
                "deviceName": "RZCT609NGNJ",
                "platformName": "Android",
                "appium:uiautomator2ServerInstallTimeout": "90000",
                "appium:appPackage": "com.flipkart.android",
                "appium:appActivity": ".SplashActivity"
            }

            self.driver = appium_driver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
            self.driver.implicitly_wait(15)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()

