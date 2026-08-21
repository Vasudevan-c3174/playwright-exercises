from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    page.get_by_role('button[data-test="nav-categories"]').click()
    page.wait_for_timeout(3000)
    print("Category page is displayed")

    tool = page.locator('a[data-test="nav-power-tools"]')
    tool.click()
    page.wait_for_timeout(3000)
    print(tool.text_content())
    
    
    product_details = page.locator(".card")
    print("prodcount", product_details.count())
    for i in range(product_details.count()):
        print(product_details.nth(i).text_content())
        

    

