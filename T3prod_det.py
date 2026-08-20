from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    page.locator('img[alt="Slip Joint Pliers"]').click()
    page.wait_for_timeout(3000)

     
    p_name =page.locator('h1[data-test="product-name"]')
    print(p_name.text_content())
    page.wait_for_timeout(3000)

    p_price = page.locator('span[aria-label="unit-price"]')
    print(p_price.text_content())  
    page.wait_for_timeout(3000)

    p_description = page.locator('p[id="description"]')
    print(p_description.text_content())
    page.wait_for_timeout(3000)

    page.locator('button[data-test="add-to-cart"]').click()
    page.wait_for_timeout(3000)

    page.wait_for_selector('fa-icon[class="ng-fa-icon px-1"]').click()
    page.wait_for_timeout(5000)

               # div data-test="product-name"
                #img alt="Combination Pliers"
             # span aria-label="unit-price"
              #  p id="description"
            
            
        
        
        
        
        
        
        
        
