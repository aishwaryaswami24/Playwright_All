from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.flipkart.com/')
    login=page.wait_for_selector('//a[@title="Login"]')
    page.wait_for_selector('//a[@title="Login"]').hover()
    page.wait_for_timeout(5000)
    browser.close()

    #mouse actions:
    #hover the dropdown
    page.wait_for_selector().hover()
    #click on element
    page.wait_for_selector().click()
    #double click on element
    page.wait_for_selector().dblclick()
    #right on element
    page.wait_for_selector().click(button='right')
    #shift click
    page.wait_for_selector().click(modifiers=['shift'])


    #keyboard actions:
    #A-Z ,a-z ,0-9,F1-F12,special char,enter,arrowdown,arrowright,pageup,control,command
    page.wait_for_selector().press('A')
    page.wait_for_selector().press('$')

