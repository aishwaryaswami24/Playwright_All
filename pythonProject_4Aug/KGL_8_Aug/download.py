from playwright.sync_api import sync_playwright


def download_handle(download):
    #in which folder want to save downloaded file and what name you want to give
    download_location='./Download/test.zip'
    download.save_as(download_location)

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.imacros.net/Automate/Downloads')
    page.on("download",download_handle)
    download=page.wait_for_selector('//a[@href="/Content/Download.zip"]').click()
    page.wait_for_timeout(5000)
    browser.close()