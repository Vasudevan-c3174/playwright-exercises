from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    # ---- Add Product A ----
    page.locator('img[alt="Slip Joint Pliers"]').click()
    page.wait_for_timeout(3000)

    price_a = float(page.locator('span[aria-label="unit-price"]').text_content().strip())
    print("Product A price:", price_a)

    add_to_cart_a = page.get_by_role('button', name='Add to Cart')
    add_to_cart_a.click()
    print(add_to_cart_a.text_content())
    page.wait_for_timeout(3000)

    page.go_back()
    page.wait_for_timeout(3000)

    # ---- Add Product B ----
    page.locator('img[alt="Bolt Cutters"]').click()
    page.wait_for_timeout(3000)

    price_b = float(page.locator('span[aria-label="unit-price"]').text_content().strip())
    print("Product B price:", price_b)

    add_to_cart_b = page.get_by_role('button', name='Add to Cart')
    add_to_cart_b.click()
    print(add_to_cart_b.text_content())
    page.wait_for_timeout(3000)

    # ---- Open cart ----
    page.locator('[data-test="nav-cart"]').click()
    page.wait_for_timeout(3000)
    expect(page.locator('[data-test="product-title"]'))

    quantities = page.locator('[data-test="product-quantity"]')

    quantity_a = float(quantities.nth(0).input_value())
    quantity_b = float(quantities.nth(1).input_value())
    print("Quantity A:", quantity_a, "Quantity B:", quantity_b)

    # ---- Dynamically calculate expected total ----
    expected_total = round((price_a * quantity_a) + (price_b * quantity_b), 2)
    print("Expected total:", expected_total)

    total_text = page.locator('[data-test="cart-total"]')
    actual_total = float(total_text.text_content().strip()[1:])
    print("Actual total:", actual_total)

    assert expected_total == actual_total
    print("Cart total is correct for initial quantities")

    # ---- Change quantity of Product A and re-verify total ----
    increase_btn_a = page.locator('button[data-test="increase-quantity"]').nth(0)
    increase_btn_a.click()
    page.wait_for_timeout(3000)

    quantity_a_updated = float(quantities.nth(0).input_value())
    print("Updated quantity of Product A:", quantity_a_updated)

    expected_total_updated = round((price_a * quantity_a_updated) + (price_b * quantity_b), 2)
    print("Expected total after quantity change:", expected_total_updated)

    actual_total_updated = float(total_text.text_content().strip()[1:])
    print("Actual total after quantity change:", actual_total_updated)

    assert expected_total_updated == actual_total_updated
    print("Cart total is correctly updated after quantity change")

    browser.close()