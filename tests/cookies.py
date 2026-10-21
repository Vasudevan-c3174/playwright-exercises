from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page =context.new_page()

    page.goto("https://www.redbus.com/")
    page.wait_for_timeout(3000)

    my_cookies = page.context.cookies()
    print(my_cookies)

   # page.context.clear_cookies()
    page.screenshot(path='test.png',full_page=True)