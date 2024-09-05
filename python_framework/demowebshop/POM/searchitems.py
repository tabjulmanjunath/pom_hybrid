from demowebshop.POM.homepage import HomePage


class SearchItems(HomePage):
    text_field=("id","small-searchterms")
    search_btn=("xpath","//input[@value='Search']")

    def find_items(self,items):
        self.send_text_to_an_element(self.text_field,items)
        self.click_on_an_element(self.search_btn)