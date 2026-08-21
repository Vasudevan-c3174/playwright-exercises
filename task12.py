from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    product_a = page.locator('img[alt="Slip Joint Pliers"]').click()
    product_price_a = page.locator('span[aria-label="unit-price"]') 
    product_price_text_a = product_price_a.text_content().strip()
    print(product_price_text_a) 
    
    add_to_cart_a = page.get_by_role('button', name='Add to Cart')
    add_to_cart_a.click()
    print(add_to_cart_a.text_content())
    page.wait_for_timeout(5000)
    

    page.go_back()
    page.wait_for_timeout(3000)

    product_b = page.locator('img[alt="Bolt Cutters"]').click()
    product_price_b = page.locator('span[aria-label="unit-price"]') 
    product_price_text_b = product_price_b.text_content().strip()
    print(product_price_text_b) 

    add_to_cart_b = page.get_by_role('button', name='Add to Cart')
    add_to_cart_b.click()
    print(add_to_cart_b.text_content())  
    page.wait_for_timeout(3000)  

    page.locator('[data-test="nav-cart"]').click()  
    expect(page.locator('[data-test="product-title"]'))
    

    # cart_product_price_a = page.locator('span[name="product-price"]').nth(0) 
    # cart_product_price_text_a = cart_product_price_a.text_content().strip()[1:]
    # print(cart_product_price_text_a)

    # cart_product_price_b=page.locator('span[data-test="product-price"]') 
    # cart_product_price_text_b = cart_product_price_b.text_content().strip()[1:]
    # page.wait_for_timeout(3000)
    # print(cart_product_price_text_b)

    # assert product_price_text_a == cart_product_price_text_a
    # assert product_price_text_b == cart_product_price_text_b
    # print("Both prices are correct")

    quantities = page.locator('[data-test="product-quantity"]')

    quantity_a = quantities.nth(0).input_value()
    quantity_b = quantities.nth(1).input_value()

    assert quantity_a == "1"
    assert quantity_b == "1"

    print("Both quantities are correct")

    # page.locator('a[class="btn btn-danger"]').click()
    # print("product removed from cart successfully")
    # page.wait_for_timeout(5000)

    

    




