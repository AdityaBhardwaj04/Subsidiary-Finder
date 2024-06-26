from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def search_subsidiaries(company_name):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(executable_path="C://chromedriver//chromedriver-win32//chromedriver.exe"), options=options)

    search_query = f"Subsidiaries for {company_name}"
    search_url = f"https://www.google.com/search?q={search_query}"

    driver.get(search_url)

    time.sleep(5)

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

    driver.quit()

    return subsidiary_names
