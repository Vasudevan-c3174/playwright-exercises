from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(2000)

    all_products = []
    page_number = 1
    first_page_products = []
    second_page_products = []

    while True:

        products = page.locator('[data-test="product-name"]')

        current_products = []

        for i in range(products.count()):
            product_name = products.nth(i).text_content().strip()
            current_products.append(product_name)

        print(f"\nPage {page_number}: {len(current_products)} products")

        for product in current_products:
            print(f" - {product}")

        
        if page_number == 1:
            first_page_products = current_products.copy()

        
        if page_number == 2:
            second_page_products = current_products.copy()

           
            assert not set(first_page_products).intersection(second_page_products), \
                "Page 1 and Page 2 contain common products"

            print("Page 1 and Page 2 products are different")

        all_products.extend(current_products)

     
        next_button = page.locator('[data-test="pagination-next"]')

       
        if next_button.count() == 0:
            break

        
        next_parent = next_button.locator("..")
        parent_class = next_parent.get_attribute("class")

        if parent_class and "disabled" in parent_class:
            break

        # Remember first product
        first_product = current_products[0]
        next_button.click()

        
        expect(
            page.locator('[data-test="product-name"]').first
        ).not_to_have_text(first_product)

        page_number += 1

    # Verify no product appears more than once
    assert len(all_products) == len(set(all_products)), \
        "Duplicate product found across pages"

    print(f"\nTotal unique products: {len(set(all_products))}")

    browser.close()