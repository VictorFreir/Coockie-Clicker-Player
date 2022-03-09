import pandas as pd
import numpy as np
from settings import browser
from format import to_float
store = pd.DataFrame({'name':['Cursor','Grandma','Farm','Mine','Factory','Bank','temple','Wizard Tower'],
        'css_tag_price':['productPrice0','productPrice1','productPrice2','productPrice3','productPrice4','productPrice5','productPrice6','productPrice7'],
        'cookie_per_seconds':[0.1,1,8,47,260,1400,7800,44000],
        'css_tag_button':['product0','product1','product2','product3','product4','product5','product6','product7'],
        'unlock_in':[0,100,1100,12000,130000,1400000,20000000,330000000],
        'unlocked':[False,False,False,False,False,False,False,False]})

def next_buy(df,time_left,cookie_per_second):
    coeficients = dict()
    if cookie_per_second == 0:
        cookie_per_second = 0.00001

    for index,row in df.iterrows():
        css_tag_price = row['css_tag_price']
        if row['unlocked']:
            price = float(browser.find_element_by_id(css_tag_price).text)
        else:
            price = row['unlock_in']
        
        time_for_buy = price/cookie_per_second
        o = row['cookie_per_seconds'] # cookie per second of option
        
        y = ((time_left - time_for_buy) * o) - (time_for_buy * cookie_per_second)
            
        coeficients[row['name']] = y
    
    max_value_name = max(coeficients,key=coeficients.get)
    select = df.loc[df['name'] == max_value_name]
    unlocked = select['unlocked'].values
    css_tag_button = select['css_tag_button'].values
    css_tag_price = select['css_tag_button'].values
    unlocked = unlocked[0]
    css_tag_button = css_tag_button[0]
    css_tag_price = css_tag_price[0]
    
    if unlocked:  # ERRO AQUI
        price = browser.find_element_by_id(css_tag_price).text.split()
        price = price[-1]
        price = to_float(price)
    else:
        price = df.loc[df['name'] == max_value_name,'unlock_in']

    return max_value_name, price, css_tag_button,df

def buy_item(css_tag_item):
    browser.find_element_by_id(css_tag_item).click()