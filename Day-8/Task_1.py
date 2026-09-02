from pathlib import Path
from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

  
    page.goto("https://www.amazon.in/")
    page.wait_for_load_state()

    #Login 
    page.locator("#nav-link-accountList-nav-line-1").click()
    page.wait_for_load_state("networkidle")

    page.locator("#ap_email_login").fill("9788842028")
    page.locator('input[type="submit"]').click()    
    page.pause()

    page.wait_for_timeout(5000)

    page.locator("#twotabsearchtextbox").fill("clean code by robert c. martin")
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    first_product = page.locator('div[data-component-type="s-search-result"]').first
    first_product.locator("a").first.click()
    print(page.title())

    page.go_back()
    page.wait_for_timeout(3000)

    account_menu = page.locator("#nav-link-accountList-nav-line-1")
    account_menu.hover()
    page.wait_for_timeout(3000)
    print("Hovered over the account menu (Hello, vasu)")
    
    
    account_menu.click()
    page.wait_for_load_state()

    page.locator('img[src*="account._CB660668669_"]').click()
    page.wait_for_timeout(3000)

    page.locator('img[src*="identity-avatar-head-n-shoulder-default"]').click()

    page.locator('#member-details-profile-picture-edit').click()
    

    with page.expect_file_chooser() as file_chooser_info:
        page.locator('#avatar-select-button-text').click()

    file_chooser = file_chooser_info.value

    file_path = r"V:\playwright\tests\playwright-exercises\photo.jpg"
    file_chooser.set_files(file_path)

    page.wait_for_timeout(2000)

    page.locator('#loading-button-2-announce').click()

   

    browser.close()
