import os, sys
sys.path.insert(0, os.path.abspath(".."))

from pytest_bdd import *
from main.utils.drivers import Driver
from main.Pages.android.languagepage import LanguagePage
from main.Pages.android.loginpage import LoginPage
from main.Pages.android.homepage import HomePage
from main.Pages.android.categoriespage import CategoriesPage

scenarios("../../Features/android/CheckAllCategories.feature")

@given(u'Flipkart app opens')
def LaunchFlipkartApp(context):
    driver = Driver("android")
    context.driver = driver.get_driver()

@given(u'English Language Selected')
def SelectEnglishLanguage(context):
    language_page = LanguagePage(context.driver)
    language_page.select_english_language()
    language_page.click_submit_button()
    assert True

@given(u'login flow skipped')
def SkipLoginFlow(context):
    login_page = LoginPage(context.driver)
    login_page.click_cancel_button()
    login_page.click_custom_back_button()
    assert True

@when(u'category page opens')
def OpenCategoriesPage(context):
    home_page = HomePage(context.driver)
    home_page.click_category_icon()
    assert True

@then(u'Verify all categories text')
def VerifyAllCategoriesText(context):
    categories_page = CategoriesPage(context.driver)
    return categories_page.check_all_category_title()

@then(u'close app')
def CloseApp(context):
    context.driver.quit()
    assert True

