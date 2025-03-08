# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser=p.chromium.launch(headless=False)
#
#     page=browser.new_page()
#     page.goto("https://www.google.com/")
#     page.pause()
#     print("Chromium browser launched successfully")
#     print(page.title())
#     page.wait_for_timeout(300)
#     browser.close()
#
#
#

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('')
    page.wait_for_timeout(2000)
    browser.close()