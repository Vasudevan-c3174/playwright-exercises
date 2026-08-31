import asyncio
from playwright.async_api import async_playwright, expect


products = ["Combination Pliers","Hammer","Screwdriver","Pliers","Bolt Cutters"]
async def main():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        
        async def search_product(product):
            page = await context.new_page()
            

            try:
                await page.goto("https://practicesoftwaretesting.com/")
                await page.locator('[data-test="search-query"]').fill(product)
                await page.locator('[data-test="search-submit"]').click()
                await page.wait_for_load_state("networkidle")


                await expect(page.locator('[data-test="product-name"]').filter(has_text=product).first).to_be_visible()
                print(f"{product} → PASS")

            except:
                print(f"{product} → FAIL - Product not found")
            await page.close()
        tasks = [search_product(product)for product in products]
        await asyncio.gather(*tasks)

        await browser.close()


asyncio.run(main())