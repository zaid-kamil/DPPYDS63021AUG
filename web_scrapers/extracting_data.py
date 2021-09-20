from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht'
driver.get(url)

# target area
target = driver.find_element_by_class_name('chart')
target = target.find_element_by_tag_name('tbody')

rows =  target.find_elements_by_tag_name('tr')
print(f"we found {len(rows)} of data")

data = []
for item in rows:
    name = item.find_element_by_css_selector('td.titleColumn').text
    week_earn = item.find_element_by_css_selector('td.ratingColumn').text
    gross_earn = item.find_elements_by_css_selector('td.ratingColumn')[-1].text 
    weeks = item.find_element_by_css_selector('td.weeksColumn').text
    data.append({
        'name': name,
        'weekend': week_earn,
        'gross': gross_earn,
        'weeks': weeks
    })
# data saving
pd.DataFrame(data).to_csv('box_office_data.csv')
