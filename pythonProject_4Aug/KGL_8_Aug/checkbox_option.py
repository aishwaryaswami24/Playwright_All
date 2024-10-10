from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    #single select
    #checkbox=page.wait_for_selector('\\input[@id="checkbox3"]')
    checkbox=page.wait_for_selector('#checkbox3')
    checkbox.click()
    if checkbox.is_checked():
        print('Passed')
    else:
        print('Failed')
    page.wait_for_timeout(4000)
    browser.close()
