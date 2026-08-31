from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_timeout(3000)


    signin = page.locator('a[href="/auth/login"]')
    expect(signin).to_be_visible()
    signin.click()
    page.wait_for_timeout(2000)
    email = page.locator("[data-test='email']")
    expect(email).to_be_visible()
    password = page.locator("[data-test='password']")
    expect(password).to_be_visible()
    email.fill("vasudevan.c@matodata.com")
    password.fill("Vasu31.7.4")
    logbtn = page.get_by_role("button",name="Login")
    expect(logbtn).to_be_visible()
    logbtn.click()
    page.wait_for_timeout(2000)



    page.goto("https://practicesoftwaretesting.com/" + "auth/login")
    page.wait_for_timeout(1500)
    email = page.locator("[data-test='email']")
    expect(email).to_be_visible()
    password = page.locator("[data-test='password']")
    expect(password).to_be_visible()
    email.fill("vasudevan.c@matodata.com")
    password.fill("xxxxxxx")
    logbtn = page.get_by_role("button",name="Login")
    expect(logbtn).to_be_visible()
    logbtn.click()
    page.wait_for_timeout(2000)


    page.goto("https://practicesoftwaretesting.com/" + "auth/login")
    page.wait_for_timeout(1500)
    email = page.locator("[data-test='email']")
    expect(email).to_be_visible()
    password = page.locator("[data-test='password']")
    expect(password).to_be_visible()    
    email.fill("vasudev.c@matodata.com")
    password.fill("Vasu31.7.4")
    logbtn = page.get_by_role("button",name="Login")
    expect(logbtn).to_be_visible()
    logbtn.click()
    page.wait_for_timeout(2000)




    page.goto("https://practicesoftwaretesting.com/" + "auth/login")
    page.wait_for_timeout(1500)
    email = page.locator("[data-test='email']")
    expect(email).to_be_visible()
    password = page.locator("[data-test='password']")
    expect(password).to_be_visible()    
    email.fill("   ")
    password.fill("   ")
    logbtn = page.get_by_role("button",name="Login")
    expect(logbtn).to_be_visible()
    logbtn.click()
    page.wait_for_timeout(2000)