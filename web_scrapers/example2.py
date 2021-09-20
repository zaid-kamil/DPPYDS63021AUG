from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht'
driver.get(url)

list_of_links = driver.find_elements_by_tag_name('a')
for link in list_of_links:
    print(link.text)

