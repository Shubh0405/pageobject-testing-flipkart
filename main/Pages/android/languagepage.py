from appium.webdriver.common.appiumby import AppiumBy

class LanguagePage:

    def __init__(self, driver):
        self.driver = driver

        self.english_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageView[1]"

        self.submit_button_id = "com.flipkart.android:id/select_btn"

    def select_english_language(self):
        self.driver.find_element(AppiumBy.XPATH, self.english_xpath).click()
        return

    def click_submit_button(self):
        self.driver.find_element(AppiumBy.ID, self.submit_button_id).click()
        return

