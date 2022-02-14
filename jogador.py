import settings
import os
import pandas as pd
from selenium.webdriver.common.by import By

browser = settings.browser
coockie = browser.find_element_by_id('bigCookie')

count_current_cookies = 0
count_total_cookies = 0


for i in range(1000):
    os.system('clear')
    coockie.click()
    count_current_cookies += 1
    count_total_cookies += 1

    

#browser.quit()
