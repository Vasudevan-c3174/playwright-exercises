from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(1000)

    
    page.locator("a[href^='/product/']").first.wait_for()  

    print("Application opened")

    
    products = page.locator("a[href^='/product/']")
    product_count = products.count()

    print("Number of products:", product_count)

   
    assert product_count > 0, "No products are displayed"
    print("Products are displayed")

   
    cheapest_price = float("inf")
    cheapest_product = ""

    
    for i in range(product_count):

        product = products.nth(i)

        
        product_name = product.locator(
            '[data-test="product-name"]'
        ).inner_text().strip()

        
       
    
    page.wait_for_timeout(3000)

    browser.close()