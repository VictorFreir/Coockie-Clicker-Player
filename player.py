from tracemalloc import start
from selenium.webdriver.common.by import By
from time import time
import pandas as pd
import settings
import format_to
import store 


browser = settings.browser
cookie = browser.find_element(By.ID,'bigCookie')

start_time = time()
minutes = 30

store = store.Store(minutes=minutes, start_time=start_time) 

while True:
    cookie.click()

    data_cookies = browser.find_element(By.ID, 'cookies').text.split()
    current_cookies = format_to.to_float(data_cookies[0])

    if current_cookies >= store.next_buy_price:
        store.buy()
        
        cookie_per_second = data_cookies[-1]
        cookie_per_second = format_to.to_float(cookie_per_second)

        store.get_current_time()
        store.next_buy(cookie_per_second)
        store.de_bug()

