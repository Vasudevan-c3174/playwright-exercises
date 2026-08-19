from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.amazon.in/")
    page.wait_for_timeout(500)
    page.locator("#nav-link-accountList-nav-line-1").click()
    page.locator("#ap_email_login").fill("9788842028")
    page.locator('input[type="submit"]').click()
    page.wait_for_timeout(5000)
    page.locator("#twotabsearchtextbox").fill("iphone 14 pro")
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="amazon_screen.png")
    page.wait_for_timeout(500000)

    browser.close()