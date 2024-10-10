# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as play:
#     browser= play.chromium.launch(headless=False)
#     page=browser.new_page()
#     page.goto("https://demo.automationtesting.in/")
#     #css selectors id= #, class=.,attribute=tagname[attribute="value"]
#     entertextbox=page.wait_for_selector("#email")
#     entertextbox.type("cdcd@gmail.com")
#     buttonlogin=page.wait_for_selector("#enterimg")
#     buttonlogin.click()
#     page.wait_for_timeout(3000)

from playwright.sync_api import sync_playwright
with sync_playwright() as play:
    browser=play.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username=page.wait_for_selector('input[placeholder="Username"]')
    username.type("Admin")
    password=page.wait_for_selector('input[placeholder="Password"]')
    password.type("admin123")
    loginbutton=page.wait_for_selector('button[type="submit"]')
    loginbutton.click()
    page.wait_for_timeout(4000)
    browser.close()











