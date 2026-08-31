from playwright.sync_api import expect, sync_playwright

products_to_search = ["Hammer", "Bolt Cutters", "Combination Pliers"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    for product_name in products_to_search:

       
        page.goto("https://practicesoftwaretesting.com/")
        page.wait_for_load_state()

        # product searched
        search = page.get_by_role("textbox", name="search")
        search.fill(product_name)
        page.keyboard.press("Enter")
        print("Search performed for:", product_name)

        # search results are displayed
        product_links = page.locator("a[href^='/product/']")
        expect(product_links.first).to_be_visible()

        product_count = product_links.count()
        assert product_count > 0, "No search results displayed"
        print("Search results are displayed")

        expected_product = None
        for i in range(product_count):
            product = product_links.nth(i)
            name = product.locator("h5").inner_text().strip()

            if product_name.lower() in name.lower():
                expected_product = product
                break

        assert expected_product is not None, f"{product_name} was not found in search results"

        expected_product.click()
        print("Product clicked")

        # product name and price are displayed
        product_name_locator = page.locator('h1[data-test="product-name"]')
        expect(product_name_locator).to_be_visible()
        actual_product_name = product_name_locator.text_content().strip()

        product_price_locator = page.locator('span[aria-label="unit-price"]')
        expect(product_price_locator).to_be_visible()
        product_price = float(product_price_locator.text_content().strip())

        print("Product name:", actual_product_name)
        print("Product price:", product_price)

        assert product_name.lower() in actual_product_name.lower(), \
            f"Wrong product details page opened. Expected: {product_name}"

        #  product to cart
        add_to_cart = page.locator('button[data-test="add-to-cart"]')
        add_to_cart.click()
        print(add_to_cart.text_content())

        # cart is opened
        page.locator('[data-test="nav-cart"]').click()
        expect(page.locator('[data-test="product-title"]')).to_be_visible()

        # Verify the correct product is in the cart
        cart_product_name = page.locator('span[data-test="product-title"]')
        cart_product_name_text = cart_product_name.text_content().strip()

        print(cart_product_name_text)

        assert cart_product_name_text == actual_product_name
        print("Correct product is present in the cart")

        # cart price matches the product price
        cart_product_price = page.locator('span[data-test="product-price"]')
        cart_product_price_text = cart_product_price.text_content().strip()[1:]

        assert float(cart_product_price_text) == product_price
        print("Cart price matches the product-page price")

        #  quantity increased by 2
        quantity = page.locator('input[data-test="product-quantity"]')
        expect(quantity).to_have_value("1")

        quantity.fill("2")
        quantity.press("Tab")

        expect(quantity).to_have_value("2")
        print("Quantity increased to 2")

        # Verify the cart total is correct
        updated_quantity = int(quantity.input_value())
        expected_total = product_price * updated_quantity

        cart_total = page.locator('[data-test="cart-total"]')

        expect(cart_total).to_have_text(f"${expected_total:.2f}")

        actual_total = float(cart_total.text_content().strip()[1:])

        print("Expected total:", expected_total)
        print("Actual total:", actual_total)

        assert expected_total == actual_total
        print("Cart total is calculated correctly:", actual_total)

        #                                product can be removed
        page.locator('a[class="btn btn-danger"]').click()
        print("Product removed from cart successfully")

        # Verify the cart is empty
        expect(page.locator('[data-test="product-title"]')).to_have_count(0)
        print("Cart is empty")

    browser.close()