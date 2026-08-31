import asyncio
import time
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright, expect


products = ["Combination Pliers","Hammer","Screwdriver","Pliers","Bolt Cutters"]

def sequential_test():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        start_time = time.perf_counter()

        for product in products:
            page = browser.new_page()
            
            page.goto("https://practicesoftwaretesting.com/")

            page.locator('[data-test="search-query"]').fill(product)
            page.locator('[data-test="search-submit"]').click()
            page.wait_for_load_state("networkidle")

            result = page.locator('[data-test="product-name"]').filter(has_text=product).first
            if result.is_visible():
                print(f"{product} → PASS")
            else:
                print(f"{product} → FAIL")           
            page.close()

        end_time = time.perf_counter()
        print(f"\nSequential execution: {end_time - start_time:.2f} seconds")

        browser.close()


async def parallel_test():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        async def search_product(product):
            
            page = await context.new_page()

            await page.goto("https://practicesoftwaretesting.com/")

            await page.locator('[data-test="search-query"]').fill(product)
            await page.locator('[data-test="search-submit"]').click()
            await page.wait_for_load_state("networkidle")

            result =  page.locator('[data-test="product-name"]').filter(has_text=product).first
            if result.is_visible():
                print(f"{product} → PASS")
            else:
                print(f"{product} → FAIL")           
            await page.close()            

        start_time = time.perf_counter()
        await asyncio.gather(*(search_product(product) for product in products))
        end_time = time.perf_counter()

        print(f"\nParallel execution: {end_time - start_time:.2f} seconds")

        await browser.close()

sequential_test()
asyncio.run(parallel_test())