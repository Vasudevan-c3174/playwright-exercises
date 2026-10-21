import uuid

import pytest
from playwright.async_api import async_playwright, expect


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

            await page.locator(
                '[data-test="register-form"]'
            ).wait_for(
                state="visible",
                timeout=10000
            )

            # 2. Generate unique email
            unique_email = (
                f"testuser_{uuid.uuid4().hex[:10]}@gmail.com"
            )

            # 3. Fill valid registration details

            await page.locator(
                '[data-test="first-name"]'
            ).fill("arun")

            await page.locator(
                '[data-test="last-name"]'
            ).fill("deepak")

            await page.locator(
                '[data-test="dob"]'
            ).fill("2003-03-13")

            await page.locator(
                '[data-test="country"]'
            ).select_option("IN")

            await page.locator(
                '[data-test="postal_code"]'
            ).fill("630606")

            await page.locator(
                '[data-test="house_number"]'
            ).fill("32-e")

            # Wait for address lookup to finish
            address_lookup = page.get_by_text(
                "Looking up your address..."
            )

            if await address_lookup.is_visible():
                await address_lookup.wait_for(
                    state="hidden",
                    timeout=10000
                )

            await page.locator(
                '[data-test="street"]'
            ).fill("pookkara street")

            await page.locator(
                '[data-test="city"]'
            ).fill("manamadurai")

            await page.locator(
                '[data-test="state"]'
            ).fill("tamilnadu")

            await page.locator(
                '[data-test="phone"]'
            ).fill("8870618311")

            await page.locator(
                '[data-test="email"]'
            ).fill(unique_email)

            await page.locator(
                '[data-test="password"]'
            ).fill("Volleyball*1303")

            # 4. Click Register
            await page.locator(
                '[data-test="register-submit"]'
            ).click()

            # 5. Verify successful registration
            await expect(
                page
            ).to_have_url(
                LOGIN_URL,
                timeout=10000
            )

        finally:
            await context.close()
            await browser.close()