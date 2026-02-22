from pages.main_page import MainPage

def test_logo_visible(page):
    main_page = MainPage(page)
    main_page.open_main()
    assert main_page.is_logo_visible()