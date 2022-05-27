import requests
import csv
from bs4 import BeautifulSoup
from time import sleep

url = 'https://alta.ge/notebooks-page-0.html'

file = open('laptops.csv', 'w', encoding='utf-8_sig', newline='\n')
f_obj = csv.writer(file)
f_obj.writerow(['Name', 'Price'])

page = 1
while page < 6:
    url = url.replace(str(page-1),str(page))
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    sub_soup = soup.find('div', class_='grid-list')
    laptops = sub_soup.find_all('div', {'class':['ty-column3', 'ty-column3 big-column-gl']})
    for each in laptops:
        laptop_name = each.find('a', class_='product-title').text
        laptop_price = each.find('span', class_='ty-price-num').text
        f_obj.writerow([laptop_name, laptop_price])
        print(laptop_name, laptop_price)
    page+=1
    sleep(15)