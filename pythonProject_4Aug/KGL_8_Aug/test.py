from playwright.sync_api import sync_playwright

def test_launch():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://www.amazon.in/')
        print(page.title())
        print('chromium browser opened successfully')
        electronics=page.wait_for_selector('a[href="/electronics/b/?ie=UTF8&node=976419031&ref_=nav_cs_electronics"]')
        electronics.click()
        search=page.wait_for_selector('input[id="twotabsearchtextbox"]')
        search.type('IPhone 13')
        search_icon=page.wait_for_selector('input[id="nav-search-submit-button"]')
        search_icon.click()
        page.wait_for_timeout(9000)
        browser.close()


def test_fib():
    # fibonacci series
    def fib_series(n):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[:n]

    n = 11
    print(fib_series(n))