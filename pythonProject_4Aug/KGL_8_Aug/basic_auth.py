# #general way
#
# from playwright.sync_api import sync_playwright,expect
# with sync_playwright() as p:
#     browser=p.chromium.launch(headless=False)
#     context=browser.new_context()
#     page=context.new_page()
#     page.goto('https://practicetestautomation.com/practice-test-login/')
#
#     page.fill('#username','student')
#     page.fill('#password','Password123')
#     page.locator('#submit').click()
#
#     # result=page.locator('//strong[text()="Congratulations student. You successfully logged in!"]').inner_text()
#     # print(result)
#
#     result = page.locator('//strong[text()="Congratulations student. You successfully logged in!"]')
#     expect(result).to_have_text('Congratulations student. You successfully logged in!')
#
#     page.wait_for_timeout(2000)
#
#     context.close()
#     browser.close()

#http auth
from playwright.sync_api import sync_playwright,expect
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context(http_credentials={'username':'admin','password':'admin'})
    page=context.new_page()
    page.goto('https://the-internet.herokuapp.com/basic_auth')
    page.wait_for_timeout(2000)
    expect(page.locator('#content p')).to_have_text('Congratulations! You must have the proper credentials.')


    context.close()
    browser.close()