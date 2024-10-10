from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')

    ## List of checkbox selectors
    # checkboxes = ['#checkbox1', '#checkbox2', '#checkbox3']
    # ##Loop through each checkbox selector
    # for selector in checkboxes:
    #     ## Wait for the checkbox element and click it
    #     checkbox = page.wait_for_selector(selector)
    #     checkbox.click()


    checkboxes = ['#checkbox1', '#checkbox2', '#checkbox3']
    for i in checkboxes:
       checkbox = page.wait_for_selector(i)
       checkbox.click()
    page.wait_for_timeout(5000)
    browser.close()