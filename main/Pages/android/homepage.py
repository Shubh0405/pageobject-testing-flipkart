from appium.webdriver.common.appiumby import AppiumBy

class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.category_icon_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]"

    def click_category_icon(self):
        self.driver.find_element(AppiumBy.XPATH, self.category_icon_xpath).click()
        return 