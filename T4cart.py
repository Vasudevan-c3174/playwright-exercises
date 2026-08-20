from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://practicesoftwaretesting.com/")

    
    page.locator('img[alt="Hammer"]').click()
    page.locator('button[data-test="add-to-cart"]').click()

   
    page.locator('[data-test="nav-cart"]').click()   
    expect(page.locator('[data-test="product-title"]')).to_have_text("Hammer")
    
    quantity = page.locator('input[data-test="product-quantity"]')
    expect(quantity).to_have_value("1")
    print(quantity.text_content())  

    page.locator('a[class="btn btn-danger"]').click()
    print("product removed from cart successfully")
    page.wait_for_timeout(5000)
    

    browser.close()
