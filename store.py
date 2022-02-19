import pandas as pd
import numpy as np
from jogador import browser
store = pd.Dataframe({'name':['Cursor','Grandma','Farm'],
        'css_tag_price':['productPrice0','productPrice1','ProductPrice2'],
        'cookie_per_seconds':[0.1,1,8],
        'css_tag_button':['Product0','Product1','Product2'],
        'unlock_in':[0,100,1100],
        'unlocked':[False,False,False]})

def next_buy(df,time_left,cookie_per_second):
    coeficients = dict()
    for index,row in df.iterrows():
        css_tag_price = df['css_tag_price']
        price = float(browser.find_element_by_id(css_tag_price))
        
        time_for_buy = price/cookie_per_second
        o = row['cookie_per_seconds'] # cookie per second of option
        y = ((time_left - time_for_buy) * o) - (time_for_buy * cookie_per_second)
        coeficients[row['name']] = y
    
    coeficients = np.array(coeficients)
    max_value_name = max(coeficients.iteritems(),key=operator.itemgetter(1))[0]
    return max_value_name