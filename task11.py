from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(1000)

    
    page.locator("a[href^='/product/']").first.wait_for()

    print("Application opened")

    # Get all products
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

        
        assert product_name != "", \
            f"Product name is empty for product {i + 1}"
        price_text = product.locator('[data-test="product-price"]').inner_text().strip()
        assert price_text != "", \
            f"Product price is empty for {product_name}"

        
        price = float(price_text.replace("$", ""))
        print(f"{product_name} - {price_text}")

        # Find cheapest product
        if price < cheapest_price:
            cheapest_price = price
            cheapest_product = product_name
    print()
    print("Cheapest Product:")
    print(f"{cheapest_product} - ${cheapest_price:.2f}")

    
    page.wait_for_timeout(3000)

    browser.close()