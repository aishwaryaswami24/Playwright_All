from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.context.tracing.start(snapshots=True,screenshots=True,sources=True)
    page.goto('https://www.google.co.in/')
    searchbox=page.wait_for_selector('//span[@class="QCzoEc z1asCe MZy1Rb"]//*[local-name()="svg"]')
    searchbox.type('Playwright')
    searchbox.press('Enter')
    page.context.tracing.stop(path='cool.zip')

    context.close()
    browser.close()

# (.venv) PS C:\Users\nagur\PycharmProjects\pythonProject\Playwright_All\Playwright_All\pythonProject_4Aug\KGL_8_Aug> python .\trace_viewer.py
# (.venv) PS C:\Users\nagur\PycharmProjects\pythonProject\Playwright_All\Playwright_All\pythonProject_4Aug\KGL_8_Aug> playwright show-trace cool.zip
