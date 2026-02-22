from pages.main_page import MainPage

def test_products_menu_visible(page):
    main_page = MainPage(page)
    main_page.open_main()
    assert main_page.is_products_menu_visible()