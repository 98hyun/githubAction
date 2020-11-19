import requests
from bs4 import BeautifulSoup

def parse(url,headers):
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.text,'html.parser')
    return soup

def extract_book_data(soup):
    upload_contents=''

    new_book_list=soup.select('div.goods_info')
    base_url='http://www.yes24.com'

    for book in new_book_list:
        title=book.select('a')[0].text
        link=book.select('a')[0]['href']
        view_link=base_url+link

        content=f"<a href={view_link}>" + title + "</a><br/>\n"
        upload_contents+=content
    return upload_contents