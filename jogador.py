import settings
import os
import pandas as pd
from selenium.webdriver.common.by import By
from time import time
from store import *
import format

browser = settings.browser
cookie = browser.find_element_by_id('bigCookie')

start_time = time()
next_buy_price = 15
next_buy_name = 'Cursor'
next_buy_css_tag = 'product0'
while True:
    
    cookie.click()
    data_cookies = browser.find_element_by_id('cookies').text.split()
    current_cookies = format.to_float(data_cookies[0])
    print(current_cookies)
    if current_cookies >= next_buy_price:
        
        buy_item(next_buy_css_tag)
        store.loc[store['name'] == next_buy_name,'unlocked'] = True # ERRO AQUI
        
        current_time = time()
        time_left = 600 - (current_time+start_time)
        
        print(data_cookies)
        cookie_per_second = data_cookies[-1]
        cookie_per_second = format.to_float(cookie_per_second)

        next_buy_name, next_buy_price, next_buy_css_tag,store = next_buy(store,time_left,cookie_per_second)
        print(f'Current cookies: {current_cookies}')
        print(f'Name item: {next_buy_name}')
        print(f'Price item: {next_buy_price}')
