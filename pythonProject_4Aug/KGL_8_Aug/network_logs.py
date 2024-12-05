from playwright.sync_api import sync_playwright

def capture_network_logs():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)  # Set headless=False to see the browser actions
        page = browser.new_page()

        # Add event listener to capture network requests
        page.on("request", lambda request: print(f"Request: {request.method} {request.url}"))

        # Add event listener to capture network responses
        page.on("response", lambda response: print(f"Response: {response.status} {response.url}"))

        # Navigate to a page
        page.goto("https://example.com")

        # Perform other actions as needed
        # e.g., interacting with elements, waiting for responses

        # Close the browser
        browser.close()

# Call the function
capture_network_logs()
