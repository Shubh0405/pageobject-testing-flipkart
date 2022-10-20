import os, sys
sys.path.insert(0, os.path.abspath(".."))

from pytest_bdd import *
from main.utils.drivers import Driver
from main.Pages.web.homepage import WebHomePage
import time


scenarios("../../Features/web/CheckLoginBox.feature")

@given(u'launch chrome browser')
def LaunchChromeBrowser(context):
    driver = Driver("web")
    context.driver = driver.get_driver()

@when(u'Flipkart home page opens')
def OpenFlipkart(context):
    context.driver.get("https://www.flipkart.com")
    time.sleep(5)
    assert True

@then(u'Verify Login Text is Present')
def VerifyLoginText(context):
    homepage = WebHomePage(context.driver)
    assert homepage.get_login_text()

@then(u'Verify username field is present')
def VerifyUsernameField(context):
    homepage = WebHomePage(context.driver)
    assert homepage.get_username_field()

@then(u'Verify password field is present')
def VerifyPasswordField(context):
    homepage = WebHomePage(context.driver)
    assert homepage.get_password_field()

@then(u'Close Browser')
def CloseBrowser(context):
    context.driver.quit()
    assert True

