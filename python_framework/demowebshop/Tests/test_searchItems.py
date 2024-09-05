from demowebshop.POM.homepage import HomePage
from demowebshop.POM.loginpage import LogIn
from demowebshop.POM.searchitems import SearchItems

def test_search_for_items(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("tabjulmanju@gmail.com", "Manju@468")
    search = SearchItems(driver)
    search.find_items("computer")
    assert driver.find_element("xpath", "//a[.='Build your own computer']").is_displayed()


