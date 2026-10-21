const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

 
await page.route('**/*.{jpg,png,jpeg,gif}',route => route.abort());
  
  await page.goto("https://www.redbus.com/");
  
  
 //// await page.waitForTimeout(5000);

 // await browser.close();
})();


// What have we done?
// How do we improve?
// 10:09 AM
// What is our next goal?
// 10:10 AM
// AI enabled playwright scripts
// 10:10 AM
// Use maestro
// 10:10 AM
// Integrating CI with playwright