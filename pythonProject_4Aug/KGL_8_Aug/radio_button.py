from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    radio_button=page.wait_for_selector('//input[@value="FeMale"]')
    radio_button.click()

    #validate wheather that option is checked or not using if statement
    if radio_button.is_checked():
        print('Passed')
    else:
        print('Failed')

    #radio_button.check()
    #radio_button-page.query_selector('//input[@value="FeMale"]')
    page.wait_for_timeout(5000)
    browser.close()
