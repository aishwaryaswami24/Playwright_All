# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     browser=p.chromium.launch(headless=False)
#     page=browser.new_page()
#     page.goto("https://demo.automationtesting.in/")
#     print("chromium browser opened successfully")
#     print(page.title())
#     #css selector: id denotes by # and class denotes by .
#     emailtextbox=page.wait_for_selector('#email')
#     emailtextbox.type("cdcbtest@gmail.com")
#     button=page.wait_for_selector('#enterimg')
#     button.click()
#     page.wait_for_timeout(5000)
#     browser.close()

    #attribute: "tagname[attribute = 'value']"
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #site loading takes time so inserted one timeout of 2sec
    page.wait_for_timeout(2000)
    username=page.wait_for_selector("input[name='username']")
    username.type('Admin')
    password=page.wait_for_selector("input[name='password']")
    password.type('admin123')
    login=page.wait_for_selector("button[type='submit']")
    login.click()
    page.wait_for_timeout(5000)
    browser.close()


    #xpath-relative xpath denotes by //
    #relative xpath: '//tagname[@attribute="value"]'

    #enclosedtext: the text between the tags and usually it's written in black color we use text method text()
    #enclosedtext: '//tagname[text()="text"]'

    #contains is a method contains()
    #contains:  '//tagname[contains(@atrribute,"value")]'
    #use contains in text method:
    #'//tagname[contains(text(),"text")]'

   #dynamic way to find ui element like aish1234 aish345 aish9098
   #1>stars-with: '//tagname[starts-with(@atribute,"aish")]'
   #2>ends-with

   #family
   #parent: //tagname[@atrribute ="value"]/parent::input[]
   #child: //tagname[@attribute="value"]/child::input[]
   #ancestor

   #sibling: //tagname[text()="text"]//following-sibling::tagname[no]