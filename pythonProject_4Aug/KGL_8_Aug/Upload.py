from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/FileUpload.html')
    file_upload= './file_upload.txt'
    upload_location=page.wait_for_selector('#input-4')
    upload_location.set_input_files(file_upload)
    page.wait_for_timeout(5000)

