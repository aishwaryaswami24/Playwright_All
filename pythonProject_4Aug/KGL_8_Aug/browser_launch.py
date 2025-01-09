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


from playwright.sync_api import sync_playwright,expect
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


def test_handle_newpage(page:Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')


    with page.expect_popup() as newpage:
        page.wait_for_selector('//a[@href="https://rahulshettyacademy.com/documents-request"]').click()
        childpage  = newpage.value
        # text=childpage.wait_for_selector('//a[@href="mailto:mentor@rahulshettyacademy.com"]').text_content()
        # print(text)
        text=childpage.locator('.red').text_content()
        print(text)

        #output:Please email us at mentor@rahulshettyacademy.com with below template to receive response

        words=text.split('at')
        print(words)
        #output:['Please email us ', ' mentor@rahulshettyacademy.com with below templ', 'e to receive response ']

        #email=words[1].split('with')[0].replace(' ','')

        #removing space using .replace method
        #instead of splitting again you can use strip method to remove trailing and leading space
        email=words[1].strip().split('with')[0]
        email=email.rstrip()
        print(email)
        assert email=='mentor@rahulshettyacademy.com'

