from pickle import TRUE
from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver

        self.login_message_xpath = "//div[@class='hKIFfL']"
        self.login_button_xpath = "//button[@class='_2KpZ6l _1sbqEe _3AWRsL']"

    def check_login_message(self):
        login_message = self.driver.find_element(By.XPATH, self.login_message_xpath)
        return login_message.text == "Login to see the items you added previously"

    def get_login_button(self):
        button_displayed = self.driver.find_element(By.XPATH, self.login_button_xpath).is_displayed()
        print("--------get login button------------")
        print(button_displayed)
        return button_displayed
