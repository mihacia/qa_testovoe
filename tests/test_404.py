def test_404_page(page):
    page.goto("https://selectel.ru/non-existing-page")
    assert "404" in page.content() or "не найдена" in page.content().lower()