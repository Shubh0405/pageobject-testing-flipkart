from selenium.webdriver.common.by import By

class WebHomePage:

    def __init__(self,driver):

        self.driver = driver

        self.logintext_xpath = "//span[@class='_36KMOx']//span[contains(text(),'Login')]"
        self.username_field_xpath = "//input[@class='_2IX_2- VJZDxU']"
        self.password_field_xpath = "//input[@type='password']"
        self.loginclosebutton_xpath = "//button[contains(text(),'✕')]"
        
        self.cart_button_xpath = "//a[@class='_3SkBxJ']"

    def get_login_text(self):
        return self.driver.find_element(By.XPATH, self.logintext_xpath).is_displayed()

    def get_username_field(self):
        return self.driver.find_element(By.XPATH, self.username_field_xpath).is_displayed()

    def get_password_field(self):
        return self.driver.find_element(By.XPATH, self.password_field_xpath).is_displayed()

    def close_login_box(self):
        self.driver.find_element(By.XPATH, self.loginclosebutton_xpath).click()

    def click_cart_button(self):
        cart_button = self.driver.find_element(By.XPATH, self.cart_button_xpath)
        self.driver.execute_script("arguments[0].click();", cart_button)