from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(2000)

    cards = page.locator(".card")
    for i in range(cards.count()):
        print(cards.nth(i).text_content())
        page.wait_for_timeout(3000)

    products = page.locator(".card")
    product_count = products.count()
    print("Number of products:", product_count)
    assert product_count > 0, "No products are available"
    for i in range(3,product_count):
        product = products.nth(i)
    
        if product.locator('[data-test="out-of-stock"]').count() > 0:
            continue
    
        expect(product).to_be_visible()
        product.click()
        page.wait_for_timeout(3000)
        break
    
    print("Product selected")

    

    
    
       
    

    browser.close()
        