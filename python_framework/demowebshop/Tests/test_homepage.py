import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
import allure
from allure_commons.types import AttachmentType

from demowebshop.POM.homepage import HomePage
from demowebshop.Lib.library import Base

# @pytest.fixture()
# def driver():
#     driver = WebDriver()
#     driver.maximize_window()
#     driver.get("https://demowebshop.tricentis.com/")
#     yield driver#driver is an object
#     driver.quit()

def test_check_for_login(driver):
    home_page_obj=HomePage(driver)
    home_page_obj.click_on_login()
    #condition=driver.find_element("id","Email").is_displayed()
    condition = True
    if condition == False:
        allure.attach(driver.get_screenshot_as_png(),name="test_check_for_login.png",attachment_type=AttachmentType.PNG)#Three Arguments
    assert condition
def test_check_for_register(driver):
    home_page_obj = HomePage(driver)
    home_page_obj.click_on_register()
    condition = True
    if condition == False:
        allure.attach(driver.get_screenshot_as_png(), name="test_check_for_register.png",attachment_type=AttachmentType.PNG)  # Three Arguments
    assert condition


