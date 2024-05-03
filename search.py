from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def search_subsidiaries(company_name):
    # Set up Chrome WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (optional)
    driver = webdriver.Chrome(service=Service(executable_path="C://chromedriver//chromedriver-win32//chromedriver.exe"), options=options)

    # Construct the search URL
    search_query = f"Subsidiaries for {company_name}"
    search_url = f"https://www.google.com/search?q={search_query}"

    # Open the search URL
    driver.get(search_url)

    # Wait for the results to load (adjust the time if needed)
    time.sleep(5)

    # Execute JavaScript function to extract and store subsidiary names
    js_code = """
    function extractSubsidiaries() {
        var subsidiaryNames = [];
        document.querySelectorAll(".EDblX .ct5Ked .WGwSK .dAassd").forEach(function(e){
            subsidiaryNames.push(e.innerText.replaceAll('\\n',' '));
        });
        return subsidiaryNames;
    }
    return extractSubsidiaries();
    """
    subsidiary_names = driver.execute_script(js_code)

    # Close the browser
    driver.quit()

    return subsidiary_names
