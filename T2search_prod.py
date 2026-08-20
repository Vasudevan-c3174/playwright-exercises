from playwright.sync_api import sync_playwright 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

  
    page.wait_for_selector('//input[@id="search-query"]').fill("tiger")
    page.wait_for_timeout(3000) 

    




    page.keyboard.press("Enter")
    page.wait_for_timeout(5000)

