from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.in/")
        

        page.locator("#twotabsearchtextbox").fill(
            "clean code by robert c. martin"
        )
        page.keyboard.press("Enter")
        

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
      

        cart = page.locator("#nav-cart")
        cart_count = cart.count()
        print("Cart locator matched:",cart_count,"element(s)")

        
        cart_product = page.get_by_text(product_name, exact=False)
        expect(cart_product).to_be_visible()
        print("Product added to cart successfully")

        cart_items = page.locator('[data-name="Active Items"]')
        expect(cart_items).to_be_visible()
        print("Cart contains the product.")


        browser.close()