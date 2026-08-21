from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    
    page.locator('img[alt="Slip Joint Pliers"]').click()
    page.wait_for_timeout(3000)

    product_name_a = page.locator('h1[data-test="product-name"]').text_content().strip()
    product_price_a = page.locator('span[aria-label="unit-price"]').text_content().strip()
    print(product_name_a, product_price_a)

    add_to_cart_a = page.get_by_role('button', name='Add to Cart')
    add_to_cart_a.click()
    print(add_to_cart_a.text_content())
    page.wait_for_timeout(3000)

    page.go_back()
    page.wait_for_timeout(3000)

   
    page.locator('img[alt="Bolt Cutters"]').click()
    page.wait_for_timeout(3000)

    product_name_b = page.locator('h1[data-test="product-name"]').text_content().strip()
    product_price_b = page.locator('span[aria-label="unit-price"]').text_content().strip()
    print(product_name_b, product_price_b)

    add_to_cart_b = page.get_by_role('button', name='Add to Cart')
    add_to_cart_b.click()
    print(add_to_cart_b.text_content())
    page.wait_for_timeout(3000)

   
    page.locator('[data-test="nav-cart"]').click()
    page.wait_for_timeout(3000)
    expect(page.locator('[data-test="product-title"]'))

  
    cart_titles = page.locator('span[data-test="product-title"]')
    expect(cart_titles).to_have_count(2)

    cart_title_a = cart_titles.nth(0).text_content().strip()
    cart_title_b = cart_titles.nth(1).text_content().strip()
    print(cart_title_a, cart_title_b)

    assert product_name_a == cart_title_a
    assert product_name_b == cart_title_b
    print("Both products are present in the cart")


    quantities = page.locator('[data-test="product-quantity"]')

    quantity_a = quantities.nth(0).input_value()
    quantity_b = quantities.nth(1).input_value()

    assert quantity_a == "1"
    assert quantity_b == "1"
    print("Both quantities are correct")

    
    cart_prices = page.locator('span[data-test="product-price"]')

    cart_price_a = cart_prices.nth(0).text_content().strip()[1:]
    cart_price_b = cart_prices.nth(1).text_content().strip()[1:]
    print(cart_price_a, cart_price_b)

    assert product_price_a == cart_price_a
    assert product_price_b == cart_price_b
    print("Both individual prices are correct")

   
    page.locator('a[class="btn btn-danger"]').first.click()
    print("product removed from cart successfully")
    page.wait_for_timeout(3000)

  
    remaining_titles = page.locator('span[data-test="product-title"]')
    expect(remaining_titles).to_have_count(1)

    remaining_title = remaining_titles.nth(0).text_content().strip()
    print(remaining_title)

    assert remaining_title == product_name_b
    print("Product B remains in the cart")

    browser.close()
