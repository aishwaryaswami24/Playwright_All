from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto('https://letzautomate.github.io/samples/eCommerce.html')
    page.wait_for_timeout(1000)

    #Fetch only column values

    # column_index=3
    # column_three_values=page.locator(f'//table[@id="productTable"]//tbody/tr/td[{column_index}]').all_text_contents()
    # print(column_three_values)



    #Fetch only one value from the output list

    # first_value=column_three_values[0] if column_three_values else None
    # print(first_value)


    #Fetch 1st row
    row_index=1
    row_values = page.locator(f'//table[@id="productTable"]//tbody/tr[{row_index}]/td').all_text_contents()
    print(row_values)

    browser.close()



