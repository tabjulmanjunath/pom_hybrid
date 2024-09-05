class HomePageLocators:
    login_link_locator = ("xpath", "//a[.='Log in']")
    register_link_locator = ("xpath", "//a[.='Register']")
class LoginPageLocators:
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")
