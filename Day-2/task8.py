from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    page.locator('img[alt="Slip Joint Pliers"]').click()
    page.wait_for_timeout(3000)

    btn = page.locator('button[data-test="increase-quantity"]')
    for i in range(2):
        btn.click()
    

    cart = page.locator('button[data-test="add-to-cart"]')
    cart.click()
    print(cart.text_content())
    page.wait_for_timeout(3000)

    page.locator('[data-test="nav-cart"]').click()   
    expect(page.locator('[data-test="product-title"]'))
    page.wait_for_timeout(3000)

    cquan = page.locator('input[data-test="product-quantity"]')
    print(cquan.input_value())
    page.wait_for_timeout(3000)

    cprice=page.locator('span[data-test="product-price"]') 
    caprice = cprice.text_content().strip()[1:]
    ca_price_float = float(caprice)
    ca_price_float_rounded = round(ca_price_float, 2)
    print(ca_price_float_rounded)

    tot_p = float(cquan.input_value()) * ca_price_float_rounded
    tot_p_rounded = round(tot_p, 2)
    print(tot_p_rounded)

    total_text = page.locator('[data-test="cart-total"]')
    actual_total = float(total_text.text_content().strip()[1:])
    print(actual_total)

    assert tot_p_rounded == actual_total
    print("both are same")
    
    



   
    browser.close() 






   
    
    