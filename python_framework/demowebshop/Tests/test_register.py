# from demowebshop.POM.homepage import HomePage
# from demowebshop.POM.registerpage import Register
#
# def test_register_with_valid_input(driver):
#     home=HomePage(driver)
#     home.click_on_register()
#     register=Register(driver)
#     register.register_an_account("Manjj","Tester","qTSSSSEngineer@gmail.com","Rabjul@468","Rabjul@468")
#     assert driver.find_element("xpath","//input[@value='Continue']").is_displayed()
#
# def test_register_without_firstname(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("", "Tester", "qaengineer@gmail.com", "Tabjul@468", "Tabjul@468")
#     assert driver.find_element("xpath","//span[contains(@for,'FirstName')]").is_displayed()
#
# def test_register_without_lastname(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("Manju", "", "qaengineer@gmail.com", "Tabjul@468", "Tabjul@468")
#     assert driver.find_element("xpath","//span[contains(@for,'LastName')]").is_displayed()
#
# def test_register_without_email(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("Manju", "Tabjul", "", "Tabjul@468", "Tabjul@468")
#     assert driver.find_element("xpath", "//span[contains(@for,'Email')]").is_displayed()
# def test_register_without_improper_email(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("Manju", "Tabjul", "qaengineers@", "Tabjul@468", "Tabjul@468")
#     assert driver.find_element("xpath", "(//span[.='Wrong email'])[2]").is_displayed()
#     #(//span[@class='required'])[3]
# def test_register_without_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("Manju", "Tabjul", "qaengineer@gmail.com", "", "Tabjul@468")
#     assert driver.find_element("xpath", "//span[contains(text(),'Password')]").is_displayed()
#
# def test_register_without_confirm_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("Manju", "Tabjul", "qaengineer@gmail.com", "Tabjul@468", "")
#     assert driver.find_element("xpath", "//span[contains(text(),'Password is required.')]").is_displayed()
#
# def test_register_without_valid_values(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("", "", "", "", "")
#     assert driver.find_element("xpath", "//span[contains(@for,'FirstName')]").is_displayed()