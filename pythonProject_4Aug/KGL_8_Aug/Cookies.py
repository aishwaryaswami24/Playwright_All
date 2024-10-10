from playwright.sync_api import sync_playwright
with (sync_playwright() as p):
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://www.naukri.com/mnjuser/profile?id=&altresid')
    #to see cookies
    cookies=page.context.cookies()
    print(cookies)

    #to clear cookies and print to check whether cookies cleared or not
    print(page.context.clear_cookies())

    #to pass new cookies to the page
    new_cookies = {
        'name':'Aishwarya',
        'company' :'TCS'
    }
    page.context.add_cookies([new_cookies])
    #to print added cookies
    print(new_cookies)

