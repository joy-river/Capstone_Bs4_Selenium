GOOGLEFORM_URL = "https://forms.gle/dzhc7ZPahiV3VyWc6"
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.93603850036717%2C%22east%22%3A-122.25136844042969%2C%22south%22%3A37.61419513901866%2C%22west%22%3A-122.61529055957031%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


header = {
    'Accept-Language': "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

while True:
    try:
        list_link = ["https://www.zillow.com" + (item.find("a", class_= "gZUDVm")['href'].replace("https://www.zillow.com", ""))for item in house_card]
        list_add = [item.find("a", class_="gZUDVm").text for item in house_card]
        list_price = [item.find("span", class_="iMKTKr").text for item in house_card]
        break
    except:
        response = requests.get(url=ZILLOW_URL, headers=header)
        zillow = BeautifulSoup(response.text, "html.parser")
        house_card = zillow.find_all(name="div", class_="property-card-data")

for i in range(len(list_add)):
    driver.get(GOOGLEFORM_URL)
    time.sleep(5)
    inputs = driver.find_elements(By.CLASS_NAME, "Xb9hP")
    inputs[0].find_element(By.TAG_NAME, "input").send_keys(list_add[i])
    inputs[1].find_element(By.TAG_NAME, "input").send_keys(list_price[i])
    inputs[2].find_element(By.TAG_NAME, "input").send_keys(list_link[i])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    time.sleep(1)

