import asyncio
import time
from playwright.async_api import async_playwright, expect


products = [
    "Combination Pliers",
    "Hammer",
    "Screwdriver",
    "Pliers",
    "Bolt Cutters"
]


async def main():

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)

        async def search_product(product):

            page = await browser.new_page()

            await page.goto("https://practicesoftwaretesting.com/")

            await page.locator('[data-test="search-query"]').fill(product)
            await page.locator('[data-test="search-submit"]').click()

            await page.wait_for_load_state("networkidle")

            result = page.locator(
                '[data-test="product-name"]'
            ).filter(has_text=product).first

            await expect(result).to_be_visible()

            print(f"{product} → PASS")

            await page.close()

        start_time = time.perf_counter()

        await asyncio.gather(
            *(search_product(product) for product in products)
        )

        end_time = time.perf_counter()

        print(f"\nParallel execution: {end_time - start_time:.2f} seconds")

        await browser.close()


asyncio.run(main())