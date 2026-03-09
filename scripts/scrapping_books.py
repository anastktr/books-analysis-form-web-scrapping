from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pandas as pd

base_url = 'https://books.toscrape.com/catalogue/category/books_1/'

page = 'https://books.toscrape.com/catalogue/category/books_1/index.html'

books_list = []


def get_rank(comp):
    map_for_rank = {
        'One': 1,
        'Two': 2,
        'Three':3,
        'Four':4,
        'Five':5
    }

    classes = comp.get('class')
    classes.pop(0)
    return map_for_rank[classes[0]]



def scrape_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    stock = soup.find('p', class_='instock availability').text.split()[-2]
    price = soup.find('p', class_='price_color').text

    page_inner = soup.find('ul', class_='breadcrumb')
    page_inner_contents = page_inner.find_all('li')
    genre = page_inner_contents[2].text
    title = page_inner_contents[3].text
    rating_component = soup.find('p', class_='star-rating')
    rating = get_rank(rating_component)
    return [title,genre,price,rating,stock]


while True:
    print(f'Scrapping page {page}')
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'lxml')


    books_per_page = soup.find_all('article', class_="product_pod")
    for book in books_per_page:
        book_url = book.h3.a['href']
        book_url = urljoin(base_url,book_url)
        book_details = scrape_details(book_url)
        print(book_details)
        books_list.append(book_details)



    button_next = soup.find('li', class_= 'next')
    if button_next:
        href = button_next.a['href']
        page = urljoin(base_url, href)
    else:
        print('FINISHED the scrapping')
        break


df = pd.DataFrame(books_list, columns= ["Title", "Genre", "Price", "Rating", "Stock"])
df.to_csv(r"C:\Users\anast\Desktop\web scraping\project\data\raw\dataset.csv", index=False)

print('DONE!!!!!!!!!!!!!!!!!')
    

   

