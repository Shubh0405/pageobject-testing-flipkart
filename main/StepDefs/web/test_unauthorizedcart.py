import os, sys
sys.path.insert(0, os.path.abspath(".."))

from pytest_bdd import *
from main.Pages.web.homepage import WebHomePage
from main.Pages.web.cartpage import CartPage
from .test_web_CheckLoginBox import *
import time

scenarios("../../Features/web/Cart_UnauthorizedUser.feature")

@when(u'cart page opens')
def OpenCartPage(context):
    home_page = WebHomePage(context.driver)
    home_page.click_cart_button()
    time.sleep(10)
    assert True

@then(u'login button and message should be displayed')
def CheckLoginButton(context):
    cart_page = CartPage(context.driver)
    res = cart_page.get_login_button()
    res2 = cart_page.check_login_message()
    print(res, res2)
    assert res and res2


