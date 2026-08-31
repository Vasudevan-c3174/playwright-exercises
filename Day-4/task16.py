from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    products = page.locator("a[href^='/product/']")
    product_count = products.count()

    print("Number of products:", product_count)
    assert product_count > 0, "No products are displayed"
    print("Products are displayed")

    cheapest_price = float("inf")
    cheapest_product = ""

    for i in range(product_count):

        product = products.nth(i)

        if product.locator('[data-test="out-of-stock"]').count() > 0:
            continue

        product_name = product.locator(
            '[data-test="product-name"]'
        ).inner_text().strip()

        product_price = product.locator(
            '[data-test="product-price"]'
        ).inner_text().strip()

        product_price = float(product_price.replace("$", ""))

        print(product_name, product_price)

        if product_price < cheapest_price:
            cheapest_price = product_price
            cheapest_product = product_name

    print("Cheapest product:", cheapest_product)
    print("Cheapest price:", cheapest_price)

    for i in range(product_count):

        product = products.nth(i)

        if product.locator('[data-test="out-of-stock"]').count() > 0:
            continue

        product_name = product.locator(
            '[data-test="product-name"]'
        ).inner_text().strip()

        if product_name == cheapest_product:
            product.click()
            break

    page.wait_for_timeout(3000)

    product_name = page.locator(
        'h1[data-test="product-name"]'
    )
    expect(product_name).to_be_visible()

    actual_product_name = product_name.text_content().strip()

    product_price = page.locator(
        'span[aria-label="unit-price"]'
    )
    actual_product_price = float(
        product_price.text_content().strip()
    )

    print("Product page name:", actual_product_name)
    print("Product page price:", actual_product_price)

    assert actual_product_name == cheapest_product
    assert actual_product_price == cheapest_price

    print("Product name and price are correct")

    add_to_cart = page.locator(
        'button[data-test="add-to-cart"]'
    )
    add_to_cart.click()

    print("Product added to cart")

    page.locator('[data-test="nav-cart"]').click()
    page.wait_for_timeout(3000)

    cart_product = page.locator(
        '[data-test="product-title"]'
    )
    expect(cart_product).to_be_visible()

    cart_product_name = cart_product.text_content().strip()

    print("Cart product:", cart_product_name)

    assert cart_product_name == cheapest_product

    print("Correct product is present in the cart")

    browser.close()