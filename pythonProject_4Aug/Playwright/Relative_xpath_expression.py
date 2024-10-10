# from playwright.sync_api import sync_playwright
# with sync_playwright() as play:
#     browser = play.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # xpath xpression: relative xpath expression and absolute xpath expression
    # relative xpath xpression=//
    # using attribute: "//tagname[@attributename='value']"

    # username = page.wait_for_selector("//input[@name='username']")
    # username.type('Admin')
    # password = page.wait_for_selector("//input[@name='password']")
    # password.type('admin123')
    # login = page.wait_for_selector("//button[@type='submit']")
    # login.click()
    # page.wait_for_timeout(5000)
    # browser.close()

""" enclosed text"""
    #using enclosed text: //tagname[text()='text']
from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # forgot = page.wait_for_selector("//p[text()='Forgot your password? ']")
    # forgot.click()
    # page.wait_for_timeout(5000)
    # browser.close()

"""contains"""
    #contains
    #contains using text
    #"//tagname[contains(text(),'value')]"
    #contains using attribute
    #//tagname[contains(@attributename,"enclosed text")]
    forgot=page.wait_for_selector("//p[contains(@text,'Forgot your ')]")
    forgot.click()
    page.wait_for_timeout(4000)



