from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://www.flipkart.com/')
    page.wait_for_timeout(2000)

    #to take screenshot
    #page.screenshot(path='screenshot.png')

    #to take full broswer screenshot
    page.set_viewport_size({"height" : 4000 , "width" : 1200})
    page.screenshot(path='full_screenshot.png', full_page=True)
