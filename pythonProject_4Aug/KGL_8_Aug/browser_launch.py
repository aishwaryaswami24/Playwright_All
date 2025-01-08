# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.google.co.in/")
#     print("Chromium browser opened successfully")
#     print(page.title())
#     page.get_by_label("Search", exact=True)
#     page.wait_for_timeout(3000)
#     browser.close()


from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto('https://letzautomate.github.io/samples/Login.html')

    username=page.wait_for_selector('//label[text()="Username"]/following-sibling::div//input')
    username.type('admin')

    password=page.wait_for_selector('//label[text()="Password"]/following-sibling::div//input')
    password.type('admin')

    login=page.wait_for_selector('//button[@type="submit"]')
    login.click()

    page.wait_for_timeout(2000)

    browser.close()

#shortcut way to launch browser
from playwright.sync_api import Page

def test_browser_launch(page:Page):
    page.goto('https://www.google.co.in/')

from playwright.sync_api import Playwright
def test_firefox_browser_launch(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.google.co.in/')


def test_launch_chromium_browser(page:Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.locator('#username').fill('rahulshettyacademy ')
    page.locator('#password').fill('learning')
    option=page.wait_for_selector('select[class="form-control"]')
    option.select_option(label='Teacher')
    page.wait_for_selector('//input[@type="checkbox"]').check()
    page.wait_for_selector('//input[@type="submit"]').click()
    page.wait_for_timeout(4000)
    browser.close()

