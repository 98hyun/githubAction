import requests
from bs4 import BeautifulSoup

url='http://www.yes24.com/24/Category/NewProductList/001001019001?sumGb=04'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

page=requests.get(url,headers=headers)
soup=BeautifulSoup(page.text,'html.parser')

new_book_list=soup.select('div.goods_info')
base_url='http://www.yes24.com'

for book in new_book_list:
    title=book.select('a')[0].text
    link=book.select('a')[0]['href']
    view_link=base_url+link
    print(title,view_link)