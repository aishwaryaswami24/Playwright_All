from playwright.sync_api import sync_playwright


def test_website_check():

    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        context.tracing.start(screenshots=True,snapshots=True,sources=True)
        page=context.new_page()
        page.goto('https://www.flipkart.com/')
        context.tracing.stop(path='trace1.zip')
        search=page.wait_for_selector('//input[@placeholder="Search for Products, Brands and More"]')

        search.click()
        search.fill('Samsung Galaxy S21')
        page.wait_for_selector('//input[@placeholder="Search for Products, Brands and More"]').press("Enter")
        page.wait_for_timeout(5000)
        browser.close()