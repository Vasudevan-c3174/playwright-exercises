from playwright.sync_api import expect, sync_playwright


products_to_search = [
    "Hammer",
    "Bolt Cutters",
    "Combination Pliers",
    "Slip Joint Pliers",
    "pliers"
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Search products

    for product_name in products_to_search:

        page.goto("https://practicesoftwaretesting.com/")
        page.wait_for_timeout(3000)

        search = page.get_by_role("textbox", name="search")
        search.fill(product_name)
        page.keyboard.press("Enter")
        print("Search performed for:", product_name)

        page.wait_for_timeout(5000)

        product_links = page.locator("a[href^='/product/']")
        expect(product_links.first).to_be_visible()

        product_count = product_links.count()
        assert product_count > 0, "No search results displayed"

        print("Search results are displayed")

        product_names = []

        for i in range(product_count):
            product = product_links.nth(i)
            name = product.locator("h5").inner_text().strip()
            product_names.append(name)

        print("Products found:")

        for name in product_names:
            print("->", name)

        # Check partial search

        if product_name.lower() == "pliers":

            for name in product_names:

                assert product_name.lower() in name.lower(), \
                    f"{product_name} not found in displayed product: {name}"

            print("All displayed products contain:", product_name)

        # Check valid search

        else:

            expected_product = None

            for i in range(product_count):

                product = product_links.nth(i)
                name = product.locator("h5").inner_text().strip()

                if product_name.lower() in name.lower():
                    expected_product = product
                    break

            assert expected_product is not None, \
                f"{product_name} was not found in search results"

            print(product_name, "appears in search results")

            result_name = expected_product.locator("h5").inner_text().strip()

            assert product_name.lower() in result_name.lower(), \
                f"Product name does not match search: {product_name}"

            print("Product name matches the search")

            expect(expected_product).to_be_visible()
            expected_product.click()

            page.wait_for_timeout(3000)

            print("Product clicked")

            product_heading = page.locator("h1")
            expect(product_heading).to_be_visible()

            actual_product_name = product_heading.inner_text().strip()

            print("Product details page:", actual_product_name)

            assert product_name.lower() in actual_product_name.lower(), \
                f"Wrong product details page opened. Expected: {product_name}"

            print("Correct product opened")

    # Check invalid search

    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    search = page.get_by_role("textbox", name="search")
    search.fill("tiger")
    page.keyboard.press("Enter")

    print("Invalid search performed")

    page.wait_for_timeout(5000)

    product_links = page.locator("a[href^='/product/']")
    product_count = product_links.count()

    assert product_count == 0, \
        "Search results are displayed for invalid search"

    print("No search results displayed for invalid search")

    browser.close()