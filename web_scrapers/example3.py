# targetting 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht'
driver.get(url)

# target area
target = driver.find_element_by_class_name('chart')
target = target.find_element_by_tag_name('tbody')
print(target.text)
