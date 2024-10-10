from playwright.sync_api import sync_playwright
with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    forgot = page.wait_for_selector("//label[contains(@placefolder,'User ')]")
    forgot.click()
    page.wait_for_timeout(4000)
