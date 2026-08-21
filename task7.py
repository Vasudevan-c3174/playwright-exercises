from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    page.locator('img[alt="Slip Joint Pliers"]').click()
    page.wait_for_timeout(3000)

     
    product_name =page.locator('h1[data-test="product-name"]')
    product_name_text = product_name.text_content().strip()
    print(product_name_text)
    
    product_price = page.locator('span[aria-label="unit-price"]') 
    product_price_text = product_price.text_content().strip()
    print(product_price_text) 
    

    

    product_description = page.locator('p[id="description"]')
    print(product_description.text_content())
   

    cart_page = page.locator('button[data-test="add-to-cart"]')
    cart_page.click()
    print(cart_page.text_content())
    
  
    page.locator('[data-test="nav-cart"]').click()  
    page.wait_for_timeout(3000) 
    expect(page.locator('[data-test="product-title"]'))

    cart_product_name=page.locator('span[data-test="product-title"]')
    cart_product_name_text = cart_product_name.text_content().strip()
    print(cart_product_name_text)
    cart_product_price=page.locator('span[data-test="product-price"]') 
    cart_product_price_text = cart_product_price.text_content().strip()[1:]
    print(cart_product_price_text)

    assert product_name_text == cart_product_name_text
    assert product_price_text == cart_product_price_text
    print("both are same")

    browser.close() 
