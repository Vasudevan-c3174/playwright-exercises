from playwright.sync_api import sync_playwright, expect


BASE_URL = "https://practicesoftwaretesting.com/"


def test_browser_history_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Start from the home page
        page.goto(BASE_URL)

        expect(page).to_have_url(BASE_URL)
        expect(page.locator("h1")).to_be_visible()

        # 2. Open the first product
        first_product = page.locator(".card").first
        first_product_name = first_product.locator(".card-title").inner_text()

        first_product.click()

        # Verify first product page
        expect(page.locator("h1")).to_contain_text(first_product_name)
        first_product_url = page.url

        # 3. Navigate to another product
        page.goto(BASE_URL)

        second_product = page.locator(".card").nth(1)
        second_product_name = second_product.locator(".card-title").inner_text()

        second_product.click()

        # Verify second product page
        expect(page.locator("h1")).to_contain_text(second_product_name)
        second_product_url = page.url

        # 4. Navigate to another section/page
        page.get_by_role("link", name="Contact").click()

        expect(page).to_have_url(lambda url: "/contact" in url)
        expect(page.locator("h1")).to_contain_text("Contact")

        # 5. Bonus: Refresh the page
        page.reload()

        expect(page.locator("h1")).to_contain_text("Contact")

        # 6. Browser history - go back to second product
        page.go_back()

        expect(page).to_have_url(second_product_url)
        expect(page.locator("h1")).to_contain_text(second_product_name)

        # 7. Browser history - go back to first product
        page.go_back()

        expect(page).to_have_url(first_product_url)
        expect(page.locator("h1")).to_contain_text(first_product_name)

        # 8. Browser history - go back to home page
        page.go_back()

        expect(page).to_have_url(BASE_URL)
        expect(page.locator("h1")).to_be_visible()

        # 9. Navigate forward to first product
        page.go_forward()

        expect(page).to_have_url(first_product_url)
        expect(page.locator("h1")).to_contain_text(first_product_name)

        # 10. Navigate forward to second product
        page.go_forward()

        expect(page).to_have_url(second_product_url)
        expect(page.locator("h1")).to_contain_text(second_product_name)

        # 11. Navigate forward to Contact page
        page.go_forward()

        expect(page).to_have_url(lambda url: "/contact" in url)
        expect(page.locator("h1")).to_contain_text("Contact")

        browser.close()