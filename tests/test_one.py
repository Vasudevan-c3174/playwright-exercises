from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    page.screenshot(path="ex1.png")
    page.wait_for_timeout(3000)
    browser.close()