from demowebshop.POM.homepage import HomePage

class Register(HomePage):
    gender=("id","gender-male")
    first_name=("id","FirstName")
    last_name=("id","LastName")
    email=("id","Email")
    password=("id","Password")
    confirm_password=("id","ConfirmPassword")
    submit=("id","register-button")

    def register_an_account(self,fN,lN,email,pwd,cpwd):
        self.click_on_register()
        self.click_on_an_element(self.gender)
        self.send_text_to_an_element(self.first_name,fN)
        self.send_text_to_an_element(self.last_name,lN)
        self.send_text_to_an_element(self.email,email)
        self.send_text_to_an_element(self.password,pwd)
        self.send_text_to_an_element(self.confirm_password,cpwd)
        self.click_on_an_element(self.submit)

