import settings
import os
import pandas as pd
from selenium.webdriver.common.by import By
from datetime import datetime
from store import *
browser = settings.browser
coockie = browser.find_element_by_id('bigCookie')

count_current_cookies = 0
count_total_cookies = 0


tempo_inicial = datetime.now().time()
print(tempo_inicial)

while True:
    os.system('clear')
    coockie.click()
    count_current_cookies += 1
    count_total_cookies += 1
    

#browser.quit()
