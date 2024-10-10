# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     browser=p.chromium.launch(headless=False)
#     context=browser.new_context()
#     page=context.new_page()
#     page.goto('https://demo.automationtesting.in/FileUpload.html')
#     upload_location=page.query_selector('#input-4')
#
#     #given absolute path
#     #file = '/Users/aishwarya/PycharmProjects/pythonProject_4Aug/KGL_8_Aug/File_upload.txt'
#
#     #relative path used txt file which is avalaible in same dirctory
#     file='./File_upload.txt'
#     upload_location.set_input_files(file)
#     page.wait_for_timeout(5000)
#     browser.close()




#download
from playwright.sync_api import sync_playwright


def download_handle(download):
    #it will create pravtic_start folder and save that downloded file as test.zip
    #download_file='./Practic_start/test.zip'

    #here i have saved downloaded file as test1.zip
    download_file ='./test1.zip'
    download.save_as(download_file)


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.imacros.net/Automate/Downloads')
    page.on('download', download_handle)
    download_location=page.query_selector('//a[@href="/Content/Download2.zip"]').click()
    page.wait_for_timeout(5000)
    browser.close()