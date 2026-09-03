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
        page.wait_for_load_state("domcontentloaded")

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
        broad_locator = page.get_by_role("button")
        button_count = broad_locator.count()
        print("Broad button locator matched:",button_count,"elements")

        if button_count > 1:

            print()
            print("Strict Mode Problem!")
            print("The locator matches multiple buttons.")
            print("Playwright cannot identify one specific button.")

        print()
        print("Searching for Add to Cart...")       
        add_to_cart = page.locator("#add-to-cart-button")

        if add_to_cart.count() == 0:
            add_to_cart = page.locator('input[name="submit.add-to-cart"]')
        
        if add_to_cart.count() == 0:
            add_to_cart = page.get_by_role("button",name="Add to cart",exact=True)

        
        if add_to_cart.count() == 0:
            add_to_cart = page.locator('input[value="Add to Cart"]')


        count = add_to_cart.count()
        print("Add to Cart locator matched:",count,"element(s)")
        if count == 0:
            raise Exception("Add to Cart button was not found")

        if count > 1:
            print("Multiple Add to Cart elements found.")
            add_to_cart = add_to_cart.first

        add_to_cart.click()
        print("Add to Cart clicked successfully")

        cart = page.locator("#nav-cart")
        cart_count = cart.count()
        print("Cart locator matched:",cart_count,"element(s)")

        cart_product = page.get_by_text(product_name,exact=False)
        if cart_product.count() > 0:
            print("Product added to cart successfully")
        else:
            print("Product name was not found exactly.")

            cart_items = page.locator('[data-name="Active Items"]')
            if cart_items.count() > 0:
                print("Cart contains the product.")
            else:
                raise Exception("Product was not found in cart")


        browser.close()