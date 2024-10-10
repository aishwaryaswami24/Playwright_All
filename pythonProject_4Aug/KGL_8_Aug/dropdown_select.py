from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')

    #1st way to give location of dropdown field
    #dropdown=page.wait_for_selector('#Skills')

    #2nd way to give location of dropdown field
    # dropdown=page.wait_for_selector("//select[@id='Skills']")
    # dropdown.select_option(label='Adobe InDesign')

    #3rd way to give location of dropdown field
    page.select_option('#Skills',label='Analytics')
    page.wait_for_timeout(5000)
    browser.close()