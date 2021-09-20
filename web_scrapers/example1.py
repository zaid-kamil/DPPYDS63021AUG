# web scraping libraries/frameworks used:
# 1. BeautifulSoup & requests
# 2. Scrapy
# 3. Selenium-python ✔

# requirements:
# pip install selenium
# pip install webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht'
driver.get(url)
