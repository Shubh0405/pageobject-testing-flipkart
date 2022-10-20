from appium.webdriver.common.appiumby import AppiumBy

class CategoriesPage:

    def __init__(self, driver):

        self.driver = driver

        self.title_action_bar_id = "com.flipkart.android:id/title_action_bar"

    def check_all_category_title(self):
        category_header = self.driver.find_element(AppiumBy.ID, self.title_action_bar_id)
        return category_header.text == "All Categories"