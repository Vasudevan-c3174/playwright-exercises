        #Task 6: Navigate Product Categories

#Open the application.
#Navigate to a product category.
#Verify that the category page is displayed.
#Verify that products are displayed.
#Verify that every displayed product belongs to the selected category.
#Bonus: Print the number of products displayed.

from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)

    page.locator('button[data-test="nav-categories"]').click()
    page.wait_for_timeout(3000)
    print("Category page is displayed")

    tool = page.locator('a[data-test="nav-power-tools"]')
    tool.click()
    print(tool.text_content())
    page.wait_for_timeout(3000)
    
    cards = page.locator(".card")
    print("prodcount", cards.count())
    for i in range(cards.count()):
        print(cards.nth(i).text_content())
        

    

