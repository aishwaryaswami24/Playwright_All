from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.co.in/")
    print("Chromium browser opened successfully")
    print(page.title())
    page.get_by_label("Search", exact=True)
    page.wait_for_timeout(3000)
    browser.close()