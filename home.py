from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page= browser.new_page()

    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    print(page.title())

    nav = page.locator('a[href="/contact"]')
    expect(nav).to_be_visible()
    print(nav.text_content()) 
    page.wait_for_timeout(3000)

    expect(page.locator('img[alt="Combination Pliers"]')).to_be_visible()
    print("product is visible")
    page.wait_for_timeout(3000)

    img = page.locator('img[alt="Pliers"]')
    img.click()
    p_name =page.locator('h1[data-test="product-name"]')
    print(p_name.text_content())
    
    page.wait_for_timeout(5000)
