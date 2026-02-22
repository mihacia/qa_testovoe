from pages.main_page import MainPage

def test_products_navigation(page):
    main_page = MainPage(page)
    main_page.open_main()
    products_button = page.locator("text=Продукты").first
    products_button.wait_for()
    products_button.click()
    dropdown = page.locator("text=Облачные серверы").first
    dropdown.wait_for()
    assert dropdown.is_visible()