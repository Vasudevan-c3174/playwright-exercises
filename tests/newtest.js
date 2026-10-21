
const {chromium} = require("playwright");
( async () => {
    const browser = await chromium.launch(

        {
            headless: false
        }

    );

    const page = await browser.newPage();
    await page.goto("https://www.amazon.in/");
    await page.waitForTimeout(500);
    await page.locator("#nav-link-accountList").click();
    await page.locator('#ap_email_login').fill("9788842028");
    await page.locator('input[type="submit"]').click();
    
    await page.waitForTimeout(25000);

    await page.locator("#twotabsearchtextbox").fill("iphone 14 pro");
    await page.keyboard.press('Enter');

    await page.waitForLoadState('networkidle');
    await page.screenshot({ path: 'amazon_screen.png' });
    await page.waitForTimeout(500000);

    await browser.close();
})();