# https://medium.com/@oguss/web-scraping-a-beginners-tips-on-how-to-inspect-websites-using-google-chrome-and-extract-required-768d24661ca0

from bs4 import BeautifulSoup
import requests

# changeable vars
html_page = requests.get('https://www.imdb.com/title/tt9426210/')

# dont change these vars
soup = BeautifulSoup(html_page.content, 'html.parser')  # retrieve web page, passes it to beautiful soup


def run_scraper():
    # >> simple title grab <<
    # title = soup.findAll('h1')
    # title = soup.find('h1')
    title = soup.find('h1').text
    print("Title: " + title)
    print("Object type of Title: " + str(type(title)))

    # >> get all names and urls relating to the cast <<
    cast_set = soup.findAll('div', {'class': 'StyledComponents__CastItemSummary-y9ygcu-7 jdroup'})
    print("Number of cast members found: " + str(len(cast_set)))
    print("Object type of cast_set: " + str(type(cast_set)))

    cast_member_count = 1
    for cast_member in cast_set:
        # print("Object type of cast_member: " + str(type(cast_member)))
        actor = cast_member.find('a', {'data-testid': 'title-cast-item__actor'})
        actor_name = actor.text
        actor_page = actor['href']
        # print("Object type of actor: " + str(type(actor)))
        print("Actor " + str(cast_member_count) + ": " + str(actor_name) + ". Has the page " + actor_page + ".")
        cast_member_count += 1
