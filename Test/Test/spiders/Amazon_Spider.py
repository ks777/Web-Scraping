#Integrating both scrapy and selenium methods

# -*- coding: utf-8 -*-
import scrapy
#from ..items import TestItem

from selenium import webdriver
#attempting to try out the Pandas Library for the Selenium portion of the task
#attempting to learn a bit more on data frames for web scrapping
import pandas as pd

#To reduce size, you can initialize your fields here instead of using Items.py
class TestItem(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    Method = scrapy.Field()

#Selenium
prod_list = []
cost_list = []
method = []
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0")

class AmazonSpider(scrapy.Spider):
    #Scrapy: User variables
    name = "Amazon_Info"
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0']

    #Scrappy
    def parse(self, response):
        items = TestItem()
        method1 = 'Scrapy'
        page = response.css('li.zg-item-immersion')
        #Scrapy: Extracting data
        #potential method if using response.xpath: product_name = response.xpath('//div[@class="p13n-sc-truncated"]/text()').extract()

        #Scrapy: In order to organize it into a csv file, will need to seperate each
        #scraped item.
        for goods in page:
            product_name = goods.css('a.a-link-normal div::text').extract()
            product_price = goods.css('span.p13n-sc-price::text').extract()
            Method = method1
            yield {'Product Name':product_name,'Product Price':product_price,'Method Used':Method}
        #Selenium
        paging = driver.find_elements_by_css_selector('li.zg-item-immersion')
        for goods in paging:
            products = goods.find_elements_by_css_selector('div.p13n-sc-truncated')[0].text
            costs = goods.find_elements_by_css_selector('span.p13n-sc-price')[0].text
            used = 'Selenium'
            prod_list.append(products)
            cost_list.append(costs)
            method.append(used)

        #Selenium: Method to convert scraped information into a csv file.
        downfront = pd.DataFrame(list(zip(prod_list, cost_list, method)), columns=['Product Name', 'Product Price', 'Method Used'])
        Amazon_Data = downfront.to_csv('Item2.csv', index=False)
        driver.close()

#Note 1:
#The instructions of the task made it seem like you would like 2 seperate
#csv files, 1 through Selenium and 1 through Scrapy. While i have provided that
#option, I would like to point out that both can be exported to 1 singular csv file.
#to do so, change:
#Amazon_Data = downfront.to_csv('Item2.csv', index=False)
#into       
#Amazon_Data = downfront.to_csv('Item.csv', index=False)

#Note 2:
#To run the entire program, treat it as if it was a Scrapy Program. This means
#you will need to run via the command prompt this order:
#scrapy crawl Amazon_Info -o items.csv
#inside your project directory

            
#Time taken to complete Project:
#3 hrs on 11/07 (2-2.5 hours playtesting and learning Scrapy and .5-1 hour programming)
#3 hrs on 11/08 (1 hour playtesting and learning Selenium + .5 hour debugging + 1.5 hour programming)

#In the end, 2-2.5 hours of coding was performed to achieve this assignment
#with an hour of debugging)

