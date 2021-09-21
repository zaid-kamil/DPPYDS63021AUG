from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

query = 'mobile'
page = 1
url = f'https://www.amazon.in/s?k={query}&page={page}'

driver.get(url)

target_area = driver.find_elements_by_css_selector('div.s-search-results')[1]
products = target_area.find_elements_by_css_selector('div.s-result-item')

print(len(products), 'were found on page')

# title - h2 tag
# limited time deal - span.a-badge-text
# sale price - span.a-price-whole 
# orignal price - span.a-price 
# isprime - span.s-prime

def get_product(item):
    '''extract detail from single product'''

    try:
        title = item.find_element_by_tag_name('h2').text
    except:
        title = None
    try:
        sprice = item.find_element_by_css_selector('span.a-price-whole').text
    except:
        sprice = None
    try:
        oprice = item.find_element_by_css_selector('span.a-price.a-price-text').text
    except:
        oprice = None
    try:
        if item.find_element_by_css_selector('span.s-prime').find_element_by_tag_name('i'):
            isprime = True
    except:
        isprime = False
    
    data =  {
        'title': title,
        'sale price': sprice,
        'original price': oprice,
        'isprime': isprime
    }

    if any(data.values()):
        return data

product_data = []
for item in products:
    data = get_product(item)
    print(data)
    if data:
        product_data.append(data)

pd.DataFrame(product_data).to_csv('amazon_scraper_mobile.csv')
driver.close()
