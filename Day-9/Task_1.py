from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.amazon.in/")
    page.wait_for_load_state()

    page.locator("#twotabsearchtextbox").fill(
        "clean code by robert c. martin"
    )
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)

    product_cards = page.locator(
        'div[data-component-type="s-search-result"][data-asin]'
    )

    print("Product cards found:", product_cards.count())

    product_card = product_cards.first

    product_name = product_card.locator("h2").inner_text()
    print("Product Name:", product_name)

    price = product_card.locator(".a-price").first.inner_text()
    print("Product Price:", price)

    description = product_card.inner_text()
    print("Product Description:")
    print(description)
    
    broad_locator = page.get_by_role(
            "button",
            name="Add to cart"
        )
    broad_count = broad_locator.count()
    print("Locator matched:", broad_count, "elements")

    if broad_count > 1:
        print("Multiple elements matched.")
        print("This locator is too broad.")
    else:
        print("Add to Cart locator count:", broad_count)

    product_link = product_card.locator("h2").locator("..")
    product_link.click()
    page.wait_for_load_state("domcontentloaded")
    print("Product details page opened")

    expect(page.locator("#productTitle")).to_be_visible()

    add_to_cart = page.locator("#add-to-cart-button")

    expect(add_to_cart).to_be_visible()
    print("Unique Add to Cart button identified")

    add_to_cart.click()
    page.wait_for_timeout(2000)

    print("Product added to cart")

    cart = page.locator("#nav-cart")
    cart.click()

    page.wait_for_load_state("domcontentloaded")
    print("Cart opened")

    cart_product = page.get_by_text(
            product_name,
            exact=False
        )

    expect(cart_product.first).to_be_visible()

    print("Product successfully verified in cart")
    print(product_name)

    browser.close()
