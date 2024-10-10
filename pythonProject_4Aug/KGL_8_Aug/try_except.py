from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    try:
     browser=p.chromium.launch(headless=False)
     context=browser.new_context()
     page=context.new_page()
     page.goto('https://www.flipkart.com/')
     page.wait_for_timeout(5000)
     #if something doesn't works in the try then it will to go except and finally
     label=page.query_selector_all('di')
     print(len(label))
     for i in label:
          print(i.get_attribute('class'))
     browser.close()
    except Exception as e:
        print(str(e))
    finally:
        print('code executed successfully')
