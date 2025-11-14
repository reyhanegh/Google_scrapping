from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

search_term = "beautifulsoup"
url = f"https://www.google.com/search?q={search_term}"

driver.get(url)

try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.tF2Cxc"))
    )
except:
    print("page not loaded")
    driver.quit()
    exit()

soup = BeautifulSoup(driver.page_source, "html.parser")

results = soup.find_all("div", class_="tF2Cxc")

with open("names.txt", "w", encoding="utf-8") as f:
    for res in results:
        title = res.find("h3")
        link = res.find("a")["href"] if res.find("a") else ""
        if title:
            print(title.get_text(strip=True), link)
            f.write(f"{title.get_text(strip=True)} | {link}\n")

driver.quit()
print("Done! Results saved in names.txt")
