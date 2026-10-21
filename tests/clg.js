const { chromium } = require('playwright');

(async () => {
    // Launch browser
    const browser = await chromium.launch({
        headless: false
    });

    // Create page
    const page = await browser.newPage();

    // Open YouTube
    await page.goto('https://www.youtube.com');

    // Search
    await page.locator('input[name="search_query"]')
              .fill('Thiagarajar College of Engineering');

    // Press Enter
    await page.keyboard.press('Enter');

    // Wait for results to load
    await page.waitForLoadState('networkidle');

    // Take screenshot
    await page.screenshot({
        path: 'youtube-results.png',
        fullPage: true
    });

    console.log('Screenshot saved as youtube-results.png');

    // Keep browser open for 10 seconds
    await page.waitForTimeout(10000);

    // Close browser
    await browser.close();
})();