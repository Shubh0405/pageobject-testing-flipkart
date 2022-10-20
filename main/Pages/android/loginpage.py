from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.cancel_button_id = "com.google.android.gms:id/cancel"
        self.custom_button_icon_id = "com.flipkart.android:id/custom_back_icon"

    def click_cancel_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, self.cancel_button_id)))
        self.driver.find_element(AppiumBy.ID, self.cancel_button_id).click()
        return

    def click_custom_back_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, self.custom_button_icon_id)))
        self.driver.find_element(AppiumBy.ID, self.custom_button_icon_id).click()
        return
