from pages.base_page import BasePage

class MainPage(BasePage):

    URL = "https://selectel.ru/"

    def open_main(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("domcontentloaded")

    def is_logo_visible(self):
        logo = self.page.locator("header").first
        logo.wait_for(timeout=15000)
        return logo.is_visible()
    
    def is_products_menu_visible(self):
        menu = self.page.locator("text=Продукты")
        return menu.count() > 0