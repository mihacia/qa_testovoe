from pages.main_page import MainPage

def test_main_page_opens(page):
    main_page = MainPage(page)
    main_page.open_main()
    assert "Selectel" in page.title()