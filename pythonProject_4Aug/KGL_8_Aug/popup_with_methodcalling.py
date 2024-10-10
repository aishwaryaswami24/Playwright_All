from playwright.sync_api import sync_playwright

dialog_box=[]

def handle_dialog_box(dialog):
    message=dialog.message
    dialog_box.append(message)
    dialog.accept()


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
    popup = page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(4000)
    #whenever dialog box appears then call handle_dialog_box method()
    page.on("dialog",handle_dialog_box)
    popup = page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    print(dialog_box[0])
    page.wait_for_timeout(5000)
    browser.close()