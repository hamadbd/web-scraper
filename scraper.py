import requests as req
import urllib.request
import time
from bs4 import BeautifulSoup as bs

url = 'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_Ghana'

res = req.get(url)
# print(res.content)
# print(res.headers)
content = res.content

soup = bs(content, 'html.parser')


# # print(soup.prettify())

# result = soup.find_all('li')

# citations = soup.find_all(title='Wikipedia:Citation needed')
# needed = len(citations)


# print(f'Number of citations needed is/are {needed}')


# print('passages needing citations are as follows')
# for item in result :
#       if item.find(title='Wikipedia:Citation needed'):
#         print(item.text, end='\n' *4)


# print(result[0].parent.text)


def get_citations_needed_count(url):
    """takes in a url from wikipedia and returns number
    of citations needed

    """

    # print(soup.prettify())

    citations = soup.find_all(title='Wikipedia:Citation needed')
    return len(citations)


def get_citations_needed_report(url):
    """Takes in URL and returns string of passage that
       needs citations
    """
    result = soup.find_all('li')

    ret_str = ''

    for passage in result:
        if passage.find(title="Wikipedia:Citation needed"):
            ret_str += f'{passage.text} \n'

    return ret_str


if __name__ == '__main__':
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))

