import settings

browser = settings.browser
coockie = browser.find_element_by_id('bigCookie')

count_current_cookies = 0
count_total_cookies = 0

'''     Name         preco     producao'''
loja = {'Cursor':['productPrice0',0.1],'Grandma':['productPrice1',1]}


for i in range(1000):
    coockie.click()
    count_current_cookies += 1
    count_total_cookies += 1
    
    button = browser.find_element_by_id('productPrice0')
    price = int(button.text)

    if count_current_cookies >=price:
        button.click()
        count_current_cookies -= price


#browser.quit()
