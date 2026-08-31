
#  Enter a product name in the search box. 
#  Perform the search. 
#  Verify that search resuls are displayed. 
#  Get all displayed product names. 
#  Verify that the expected product appears in the results. 
#  Click the product. 
#  Verify that the product details page contains the expected product name. 

from playwright.sync_api import expect, sync_playwright 

products_to_search = ["Bolt Cutters", "Combination Pliers", "Hammer"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    for product_name in products_to_search:

        page.goto("https://practicesoftwaretesting.com/")
        page.wait_for_timeout(3000)

        search = page.get_by_role("textbox", name="search")
        search.fill(product_name)
        print("Product_name:", product_name)
        page.keyboard.press("Enter")
        print("Search performed")

        product_links = page.locator("a[href^='/product/']")
        expect(product_links.first).to_be_visible()
        product_count = product_links.count()
        print("Number of search results:", product_count)
        assert product_count > 0, \
            "No search results displayed"
        print("Search results are displayed")        

        product_names = []
        for i in range(product_count):
            product = product_links.nth(i)
            name = product.locator("h5").inner_text().strip()
            product_names.append(name)
        print("Products found:")
        for name in product_names:
            print("->", name)

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

        expect(expected_product).to_be_visible()
        expected_product.click()
        page.wait_for_timeout(2000)
        print("Product clicked")

        product_heading = page.locator("h1")
        expect(product_heading).to_be_visible()
        actual_product_name = product_heading.inner_text().strip()
        print("Product details page:", actual_product_name)

        assert product_name.lower() in actual_product_name.lower(), \
            f"Wrong product details page opened. Expected: {product_name}"
        print("Product name verified successfully")
    browser.close()























        # product_name = page.locator(".card")
        # page.wait_for_timeout(3000)
        # for i in range(product_name.count()):
        #     print(product_name.nth(i).text_content())
        





    
