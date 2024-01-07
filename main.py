# Create a google form


# 1) import packages
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


YOUR_FORM_LINK = ""

SEARCH = "Vellore Vaughan"
# URL ="https://www.zillow.com/homes/for_rent/"

# zillow link
URL ="https://www.zillow.com/vellore-vaughan-on/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-79.68977476281738%2C%22east%22%3A-79.48893095178222%2C%22south%22%3A43.78750094132323%2C%22north%22%3A43.88779531301673%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A795873%2C%22regionType%22%3A8%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,ta;q=0.8"
}

# 2) response from zillow
response = requests.get(URL,headers=header)
html = response.text
# print(html)

# 3) soup Creation
soup = BeautifulSoup(html,"lxml")
# print(soup.prettify())

# 4) directly selecting price tag value
price = [i.text for i in soup.css.iselect(".PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1.iMKTKr")]
# print(price)


# formatting price value through iteration
prices = []
for i in price:
    a = i.split("C")
    b = a[1]
    c = b.split("/")
    prices.append(c[0])
print(prices)


# 5) selecting address tag
address = soup.find_all("address")
# print(address)

# selecting address tag value through iteration
full_address = []
for i in address:
    # print(i.text)
    full_address.append(i.text)
print(full_address)


# 6) selecting a tag values
links = [i['href'] for i in soup.css.iselect(".property-card-link")]
print(links)



# 7) Option Creation
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

# 8) Driver Creation
driver = webdriver.Chrome(option)
driver.maximize_window()
driver.get(YOUR_FORM_LINK)


# 9) loop the Entry job as the length of data list
for i in range(0,len(prices)):
    # questions 1
    WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div["
                                                                         "2]/div[1]/div/div/div[2]/div/div[1]/div/div["
                                                                         "1]/input"))).send_keys(address[i])
    # questions 2
    WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div["
                                                                         "2]/div[2]/div/div/div[2]/div/div[1]/div/div["
                                                                         "1]/input"))).send_keys(prices[i])
    # questions 3
    WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div["
                                                                         "2]/div[3]/div/div/div[2]/div/div[1]/div/div["
                                                                         "1]/input"))).send_keys(links[i])
    # submit
    WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div["
                                                                         "3]/div[1]/div[1]/div"))).click()
    # submit another response
    WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[4]/a"))).click()





# Finally check your google form for all the data