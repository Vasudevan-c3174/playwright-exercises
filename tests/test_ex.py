from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.amazon.com/")
    page.wait_for_timeout(3000)

  
    page.wait_for_selector('//input[@placeholder="Search Amazon"]').fill("iphone")

    
    page.wait_for_timeout(3000)
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)