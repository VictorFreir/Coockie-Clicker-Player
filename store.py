import pandas as pd
import numpy as np
from settings import browser
store = pd.Dataframe({'name':['Cursor','Grandma','Farm','Mine','Factory','Bank','temple','Wizard Tower'],
        'css_tag_price':['productPrice0','productPrice1','productPrice2','productPrice3','productPrice4','productPrice5','productPrice6','productPrice7'],
        'cookie_per_seconds':[0.1,1,8,47,260,1400,7800,44000],
        'css_tag_button':['product0','product1','product2','product3','product4','product5','product6','product7'],
        'unlock_in':[0,100,1100,12000,130000,1400000,20000000,330000000],
        'unlocked':[False,False,False,False,False,False,False,False]})

def next_buy(df,time_left,cookie_per_second):
    coeficients = dict()
    for index,row in df.iterrows():
        css_tag_price = df['css_tag_price']
        if row['unlocked']:
            price = float(browser.find_element_by_id(css_tag_price))
        else:
            price = row['unlock_in']
            row['unlocked'] = True
            
        time_for_buy = price/cookie_per_second
        o = row['cookie_per_seconds'] # cookie per second of option
        
        y = ((time_left - time_for_buy) * o) - (time_for_buy * cookie_per_second)
        coeficients[row['name']] = y
    
    coeficients = np.array(coeficients)
    max_value_name = max(coeficients.iteritems(),key=operator.itemgetter(1))[0]
    return max_value_name