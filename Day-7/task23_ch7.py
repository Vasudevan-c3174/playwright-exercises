import uuid

import pytest
from playwright.async_api import async_playwright, expect


BASE_URL = "https://practicesoftwaretesting.com"

@pytest.mark.asyncio                                                     # this line tells "Run this test inside an asyncio event loop."
async def test_product_search():

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            await page.goto(BASE_URL)

            # Search for Hammer
            search_box = page.get_by_placeholder("Search")

            await search_box.fill("Hammer")
            await page.get_by_role("button",name="Search").click()

            # Verify Hammer appears
            await expect(page.get_by_text("Hammer",exact=True).first).to_be_visible()

        finally:
            await context.close()
            await browser.close()

# you dont need to call each functions
# pytest automatically finds and calls functions whose names start with asyn deftest_.

@pytest.mark.asyncio
async def test_product_details():

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            await page.goto(BASE_URL)

            # Search for Hammer
            await page.get_by_placeholder("Search").fill("Hammer")
            await page.get_by_role("button",name="Search").click()

            # Open Thor Hammer
            product = page.get_by_role("link",name="Thor Hammer",exact=False)
            await expect(product).to_be_visible()
            await product.click()

            # Verify product name
            await expect(page.get_by_role("heading",name="Thor Hammer",exact=True)).to_be_visible()

            # Verify price
            await expect(page.get_by_text("$11.14",exact=True)).to_be_visible()

            # Verify description
            await expect(page.get_by_text("The legendary Thor Hammer combines premium craftsmanship",exact=False)).to_be_visible()

            # Verify Add to Cart button
            await expect(page.get_by_role("button",name="Add to cart",exact=True)).to_be_visible()

        finally:
            await context.close()
            await browser.close()

@pytest.mark.asyncio
async def test_product_category():

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            await page.goto("https://practicesoftwaretesting.com/")

            # Open Categories
            await page.locator('button[data-test="nav-categories"]').click()

            print("Category menu is displayed")

            # Select Power Tools category
            tool = page.locator('a[data-test="nav-power-tools"]')
            await expect(tool).to_be_visible()
            await tool.click()

            print("Selected category:", await tool.text_content())

            # Verify products are displayed
            product_details = page.locator(".card")

            await expect(product_details.first).to_be_visible()

            product_count = await product_details.count()

            assert product_count > 0, \
                "No products are displayed"

            print(
                "Number of products:",
                product_count
            )

            # Verify products belong to selected category
            for i in range(product_count):

                product = product_details.nth(i)

                await expect(product).to_be_visible()
                product_name = await product.locator("h5").inner_text()
                print("Power Tools product:",product_name )

        finally:
            await context.close()
            await browser.close()



REGISTER_URL = "https://practicesoftwaretesting.com/auth/register"
LOGIN_URL = "https://practicesoftwaretesting.com/auth/login"


@pytest.mark.asyncio
async def test_registration():

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        try:

            # 1. Open registration page
            await page.goto(REGISTER_URL)

            page.locator('[data-test="register-form"]')

            # 2. Generate unique email
            unique_email = (f"testuser_{uuid.uuid4().hex[:10]}@gmail.com")

            # 3. Fill valid registration details

            await page.locator(
                '[data-test="first-name"]'
            ).fill("vasu")

            await page.locator(
                '[data-test="last-name"]'
            ).fill("devan")

            await page.locator(
                '[data-test="dob"]'
            ).fill("2003-03-13")

            await page.locator(
                '[data-test="country"]'
            ).select_option("IN")

            await page.locator(
                '[data-test="postal_code"]'
            ).fill("630559")

            await page.locator(
                '[data-test="house_number"]'
            ).fill("32")

            await page.locator(
                '[data-test="street"]'
            ).fill("matha street")

            await page.locator(
                '[data-test="city"]'
            ).fill("sivagangai")

            await page.locator(
                '[data-test="state"]'
            ).fill("tamilnadu")

            await page.locator(
                '[data-test="phone"]'
            ).fill("9876543210")

            await page.locator(
                '[data-test="email"]'
            ).fill(unique_email)

            await page.locator(
                '[data-test="password"]'
            ).fill("Vasu31.7.4")

            # 4. Click Register
            await page.locator(
                '[data-test="register-submit"]'
            ).click()

            # 5. Verify successful registration
            await expect(
                page
            ).to_have_url(
                LOGIN_URL,
               
            )

        finally:
            await context.close()
            await browser.close()