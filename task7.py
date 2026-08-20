from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    page.locator('img[alt="Slip Joint Pliers"]').click()
    page.wait_for_timeout(3000)

     
    p_name =page.locator('h1[data-test="product-name"]')
    paname = p_name.text_content().strip()
    print(paname)
    #page.wait_for_timeout(3000)
    p_price = page.locator('span[aria-label="unit-price"]') 
    paprice = p_price.text_content().strip()
    print(paprice) 
    #page.wait_for_timeout(3000)

    

    p_description = page.locator('p[id="description"]')
    print(p_description.text_content())
    #page.wait_for_timeout(3000)

    cart = page.locator('button[data-test="add-to-cart"]')
    cart.click()
    print(cart.text_content())
    page.wait_for_timeout(3000)
  
    page.locator('[data-test="nav-cart"]').click()   
    expect(page.locator('[data-test="product-title"]'))
    page.wait_for_timeout(3000)

    cname=page.locator('span[data-test="product-title"]')
    caname = cname.text_content().strip()
    print(caname)
    cprice=page.locator('span[data-test="product-price"]') 
    caprice = cprice.text_content().strip()[1:]
    print(caprice)

    assert paname == caname
    assert paprice == caprice
    print("both are same")

    browser.close() 