from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')
    page.wait_for_selector('//button[contains(text(),"    click   ")]').click()
    # page.wait_for_selector('//button[(text()="    click   "]').click()

    page.wait_for_timeout(9000)
    total_pages=context.pages
    print(len(total_pages))
    for i in total_pages:
        print(i)

    #wants to store new page and close that new page tab

    new_page=total_pages[1]
    #how to switch to new page/child
    new_page.bring_to_front()
    print(new_page.title())
    #parent to front
    page.bring_to_front()
    new_page.close()
    browser.close()

# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto('https://demo.automationtesting.in/Windows.html')
#     page.wait_for_selector('//button[contains(text(),"    click   ")]').click()
#     page.wait_for_timeout(3000)
#     total_pages = context.pages
#     print(len(total_pages))
#     for i in total_pages:
#         print(i)
#     print(page.title())
#     new_page = total_pages[1]
#     new_page.bring_to_front()
#     page.wait_for_timeout(3000)
#     print(new_page.title())
#     new_page.close()
