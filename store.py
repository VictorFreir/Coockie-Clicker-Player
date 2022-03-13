from selenium.webdriver.common.by import By
from time import time
from settings import browser
import pandas as pd
import format_to

class Store:
    def __init__(self,minutes,start_time):
        self.menu = pd.read_csv('menu.csv')
        self.start_time = start_time
        self.total_time = 60*minutes
        self.browser = browser
        self.next_buy_name = 'Cursor'
        self.next_buy_price = 15.0
        self.next_buy_css_tag_button = 'product0'
        self.next_buy_css_tag_price = 'productPrice0'
        print(self.menu)

    def buy(self):
        self.browser.find_element(By.ID, self.next_buy_css_tag_button).click()
        self.menu.loc[self.menu['name'] == self.next_buy_name, 'unlocked'] = True
        self.update_price()

    def update_price(self):
        new_price = browser.find_element(By.ID,self.next_buy_css_tag_price).text
        new_price = format_to.to_float(new_price)
        self.menu.loc[self.menu['name'] == self.next_buy_name, 'price'] = new_price
        print(self.menu)

    def get_current_time(self):
        self.current_time = int(time()) - self.start_time
        self.time_left = self.total_time - self.current_time
        
    def next_buy(self,cookie_per_second):
        self.coeficients = dict()
        if cookie_per_second == 0:
            cookie_per_second = 0.0001
        
        for index,row in self.menu.iterrows():
            css_tag_price = row['css_tag_price']
            price = row['price']
            
            time_for_buy = price/(cookie_per_second*2)
            o = row['cookie_per_seconds'] # cookie per second of option
                
            y = ((self.time_left - time_for_buy) * o)
            self.coeficients[row['name']] = y
        
        self.get_max_value()


    def get_max_value(self):
        max_value = -100000
        self.max_value_name = 0
        
        for key, value in self.coeficients.items():
            if value > max_value:
                self.max_value_name = key

        self.max_item = self.menu[self.menu['name'] == self.max_value_name]
        self.get_items_from_max()

    def get_items_from_max(self):
        self.next_buy_css_tag_button = self.max_item['css_tag_button'].values
        self.next_buy_css_tag_price = self.max_item['css_tag_price'].values
        self.next_buy_price = self.max_item['price'].values
        self.next_buy_name = self.max_item['name'].values

        print(self.max_item)
        self.next_buy_css_tag_button = self.next_buy_css_tag_button[0]
        self.next_buy_css_tag_price = self.next_buy_css_tag_price[0]
        self.next_buy_price = self.next_buy_price[0]
        self.next_buy_name = self.next_buy_name[0]
        
    def de_bug(self):
        print()
        print(f'self.next_buy_name: {self.next_buy_name}')
        print(f'self.next_buy_price: {self.next_buy_price}')
        print()