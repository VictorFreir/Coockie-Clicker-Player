from selenium import webdriver
from time import sleep

url = 'https://orteil.dashnet.org/cookieclicker/'
tempo = 15

browser = webdriver.Firefox()
browser.get(url)

sleep(tempo)

