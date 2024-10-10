from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')

    #click on pop-up button by default okay cliked by playwright
    # popup=page.wait_for_selector('//div[@id="OKTab"]/button')
    # popup.click()

    popup=page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(4000)

    #before clicking on anything am teaching my code don't do anything on your own
    #dialong accept means okay
    #page.on("dialog",lambda dialog : dialog.accept())

    #dialog cancel means dismiss
    page.on("dialog",lambda dialog : dialog.dismiss())

    #print meassge on the dialog box
    page.on("dialog",lambda dialog : print(dialog.message))
    popup = page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    page.wait_for_timeout(5000)
    browser.close()