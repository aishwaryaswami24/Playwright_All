from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://www.flipkart.com/')
    page.wait_for_timeout(5000)

    #get all links which uses anchor tag with href attribute
    #links=page.query_selector_all('a') #used for anchor tag a
    links = page.query_selector_all('b')
    print(len(links))

    for i in links:
        #print(i.get_attribute('href')) #to get all href attribute in the website
        print(i.text_content())

    page.wait_for_timeout(4000)

