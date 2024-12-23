from playwright.sync_api import sync_playwright

from Playwright.code1 import first_value

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto('https://letzautomate.github.io/samples/eCommerce.html')
    page.wait_for_timeout(1000)

    column_index=3
    column_three_values=page.locator(f'//table[@id="productTable"]//tbody/tr/td[{column_index}]').all_text_contents()
    print(column_three_values)

    browser.close()

    #Fetch only one value from the output list

    first_value=column_three_values[0] if column_three_values else None
    print(first_value)

