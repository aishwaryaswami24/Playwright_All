from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')
    page.wait_for_timeout(5000)

    #find out web table location
    table=page.wait_for_selector('#customers')
    #find out total rows of table
    tr=table.query_selector_all('tr')
    print(len(tr))
    # find out total data of table
    td=table.query_selector_all('td')
    print(len(td))
    # find out total headings of table
    th=table.query_selector_all('th')
    print(len(th))

    for row in tr:
       cells = row.query_selector_all('td')
       for cell in cells:
        print(cell.text_content())


    page.wait_for_timeout(2000)
    browser.close()