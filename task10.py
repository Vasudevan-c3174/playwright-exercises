from playwright.sync_api import sync_playwright 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    src = page.locator('//input[@id="search-query"]')
    src.fill("hammer")
    print(src.input_value())
    page.wait_for_timeout(3000)

    page.keyboard.press("Enter")    

    cards = page.locator(".card")
    for i in range(cards.count()):
        print(cards.nth(i).text_content())
    page.wait_for_timeout(3000)





    
