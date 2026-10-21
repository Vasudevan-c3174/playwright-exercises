
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
    await page.locator("#nav-link-accountList-nav-line-1").click();
    await page.locator('#ap_email_login').fill("9788842028");
    await page.locator('input[type="submit"]').click();
    
    await page.waitForTimeout(5000);

    await page.locator("#twotabsearchtextbox").fill("iphone 14 pro");
    await page.keyboard.press('Enter');

    await page.waitForLoadState('networkidle');
    await page.screenshot({ path: 'amazon_screen.png' });
    await page.waitForTimeout(500000);

    await browser.close();
})();


/*  xpath - Relative xpath '//'
Using attribute - //tagname[@attributename ="value"]
text - //tagname[text()="text"]
contains
attributes - //tagname[contains(@attribute,"value")]
//input[contains(@placeholder,"User")]
dynamic - prasanth123,prasanth13454,prasanth987
starts-with - //tagname[starts-with(@id,'prasanth')]
ends-with - 2343user
family
parent - //tagname[@id = "xy"]/parent::input[]
child - //tagname[@id = "xy"]/child::input[]
ancestor -  //tagname[@id = "xy"]/ancestor::input[]
sibling - //td[text()="Microsoft"]//following-sibling:: td[2] */