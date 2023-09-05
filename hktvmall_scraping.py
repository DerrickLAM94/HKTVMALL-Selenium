from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import TimeoutException
import os

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

urls = [
        "https://www.hktvmall.com/hktv/zh/%E6%AF%8D%E5%AC%B0%E8%82%B2%E5%85%92/%E5%AC%B0%E5%85%92%E5%A5%B6%E7%B2%89/main/search?q=%3Arelevance%3Astreet%3Amain%3Acategory%3AAA28050000000", #奶粉
        "https://www.hktvmall.com/hktv/zh/%E6%AF%8D%E5%AC%B0%E8%82%B2%E5%85%92/%E5%B0%BF%E7%89%87-%E5%AD%B8%E7%BF%92%E8%A4%B2/main/search?page=0&q=%3Arelevance%3Acategory%3AAA28101000000%3Azone%3Amothernbaby%3Astreet%3Amain%3A", #紙尿片
        "https://www.hktvmall.com/hktv/zh/%E6%AF%8D%E5%AC%B0%E8%82%B2%E5%85%92/%E5%B0%BF%E7%89%87-%E5%AD%B8%E7%BF%92%E8%A4%B2/main/search?page=0&q=%3Arelevance%3Acategory%3AAA28221500000%3Azone%3Amothernbaby%3Astreet%3Amain%3A", #奶樽 奶樽蓋
        "https://www.hktvmall.com/hktv/zh/%E6%AF%8D%E5%AC%B0%E8%82%B2%E5%85%92/%E5%B0%BF%E7%89%87-%E5%AD%B8%E7%BF%92%E8%A4%B2/main/search?page=0&q=%3Arelevance%3Acategory%3AAA28270000000%3Azone%3Amothernbaby%3Astreet%3Amain%3A" #母乳餵哺用品 
        "https://www.hktvmall.com/hktv/zh/%E6%AF%8D%E5%AC%B0%E8%82%B2%E5%85%92/%E5%B0%BF%E7%89%87-%E5%AD%B8%E7%BF%92%E8%A4%B2/main/search?page=0&q=%3Arelevance%3Acategory%3AAA28320000000%3Azone%3Amothernbaby%3Astreet%3Amain%3A", #嬰兒醫藥 護膚
        "https://www.hktvmall.com/hktv/zh/%E6%AF%8D%E5%AC%B0%E8%82%B2%E5%85%92/%E5%B0%BF%E7%89%87-%E5%AD%B8%E7%BF%92%E8%A4%B2/main/search?page=0&q=%3Arelevance%3Acategory%3AAA28570500001%3Azone%3Amothernbaby%3Astreet%3Amain%3A", #嬰兒床
        "https://www.hktvmall.com/hktv/zh/%E6%AF%8D%E5%AC%B0%E8%82%B2%E5%85%92/%E5%B0%BF%E7%89%87-%E5%AD%B8%E7%BF%92%E8%A4%B2/main/search?page=0&q=%3Arelevance%3Acategory%3AAA28470505001%3Azone%3Amothernbaby%3Astreet%3Amain%3A", # 嬰兒車 
        "https://www.hktvmall.com/hktv/zh/%E6%AF%8D%E5%AC%B0%E8%82%B2%E5%85%92/%E5%B0%BF%E7%89%87-%E5%AD%B8%E7%BF%92%E8%A4%B2/main/search?page=0&q=%3Arelevance%3Acategory%3AAA28720000000%3Azone%3Amothernbaby%3Astreet%3Amain%3A"# 孕婦清潔護理

]

all_product_info = []

for i, url in enumerate(urls):
    driver.get(url)
    target_number = 1000

    while len(all_product_info) < target_number:
        elements = driver.find_elements(By.XPATH, '//div[@class="product-brief"]')

        for product in elements:
            if len(all_product_info) >= target_number:
                break

            product_info = {}

            try:
                product_info['name'] = product.find_element(By.XPATH, './/div[@class="brand-product-name"]').text
            except NoSuchElementException:
                product_info['name'] = 'NA'
            
            try:
                product_info['packing'] = product.find_element(By.XPATH, './/div[@class="packing-spec"]').text
            except NoSuchElementException:
                product_info['packing'] = 'NA'

            try:
                product_info['sold'] = product.find_element(By.XPATH, './/div[@class="salesNumber-container"]').text
            except NoSuchElementException:
                product_info['sold'] = 'NA'

            try:
                product_info['original_price'] = product.find_element(By.XPATH, './/div[@class="promotional"]').text
            except NoSuchElementException:
                product_info['original_price'] = 'NA'

            try:
                product_info['promo_price'] = product.find_element(By.XPATH, './/div[@class="price"]').text
            except NoSuchElementException:
                product_info['promo_price'] = 'NA'
            
            try:
                product_info['discount'] = product.find_element(By.XPATH, './/a[@class="linkText"]/span').text
            except NoSuchElementException:
                product_info['discount'] = 'NA'

            try:
                product_info['store_name'] = product.find_element(By.XPATH, './/a[@class="store-name-label crown"]/span').text
            except NoSuchElementException:
                product_info['store_name'] = 'NA'

            try:
                product_info['url'] = product.find_element(By.CSS_SELECTOR, '.product-brief > a').get_attribute("href")
            except NoSuchElementException:
                product_info['url'] = 'NA'

            try:
                product_info['img'] = product.find_element(By.TAG_NAME, 'img').get_attribute("src")
            except NoSuchElementException:
                product_info['img'] = 'NA'

            try:
                product_info['review'] = product.find_element(By.XPATH, './/span[@class="review-number"]').text
            except NoSuchElementException:
                product_info['review'] = 'NA'
            
            try:
                rating_element = driver.find_element(By.CSS_SELECTOR, 'div#ui-star')
                rating = rating_element.get_attribute('data-rating')
                product_info['rating'] = rating
            except NoSuchElementException:
                product_info['rating'] = 'NA'

            all_product_info.append(product_info)

        if len(all_product_info) < target_number:

            try:
                next_page_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//a[@class="next-btn"]'))
                )
            except NoSuchElementException:
                break


    df = pd.DataFrame(all_product_info)
    filename = f"data_{i}.csv"  # Use index as part of the filename
    filepath = os.path.join("/Users/derricklam/Desktop/JDE7/selenium/MidTermProject/MidTermTest/0821", filename)  # Specify the output folder path
    df.to_csv(filepath, index=False)

    # Clear the product information list for the next URL
    all_product_info.clear()

driver.quit()