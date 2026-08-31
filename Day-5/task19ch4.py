from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    products = page.locator("a[href^='/product/']")

    assert products.count() >= 5

    for i in range(5):

        products = page.locator("a[href^='/product/']")
        product = products.nth(i)

        listing_name = product.locator('[data-test="product-name"]').text_content().strip()
        listing_price = product.locator('[data-test="product-price"]').text_content().strip().replace("$", "")
        print("Listing Name :", listing_name)
        print("Listing Price:", listing_price)
        product.click()
        page.wait_for_timeout(3000)

        
        details_name = page.locator('h1[data-test="product-name"]').text_content().strip()
        details_price = page.locator('span[aria-label="unit-price"]').text_content().strip().replace("$", "")
        print("Details Name :", details_name)
        print("Details Price:", details_price)
   
        assert listing_name == details_name
        assert listing_price == details_price

        print("Result: PASS")

        page.go_back()
        page.wait_for_timeout(2000)

    print("\nAll 5 products passed")

    browser.close()