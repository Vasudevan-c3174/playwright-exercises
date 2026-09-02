from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.amazon.in/")
    page.wait_for_load_state()

    page.locator("#twotabsearchtextbox").fill(
        "clean code by robert c. martin"
    )

    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)

    first_product = page.locator(
        'div[data-component-type="s-search-result"]'
    ).first

    first_product.locator("h2 a").click()

    product_url = page.url
    print("Product URL:", product_url)
    print("Product Title:", page.title())

    page.go_back()
    page.wait_for_timeout(3000)

    print("Back to search results:", page.url)

    page.locator("#nav-link-accountList-nav-line-1").evaluate("""
        element => {
            element.addEventListener("mouseenter", () => {
                element.setAttribute("data-hovered", "true");
            });
        }
    """)

    print("Move your mouse over the Account menu...")

    page.wait_for_function("""
        () => document.querySelector("#nav-link-accountList-nav-line-1")
            ?.getAttribute("data-hovered") === "true"
    """, timeout=10000)

    print("Mouse hover event completed")

    browser.close()