gitimport requests
from bs4 import BeautifulSoup
 
def parse_link(linkge,array):
    reqs = requests.get(linkge)
    content = reqs.text
    soup = BeautifulSoup(content, 'html.parser')
    for h in soup.findAll('div',{"class":"product-item-details"}):
        a = h.find('a')
        try:
            print('got to h2 checking')
            if('title') in a.attrs:
                print('found href')
                urlge = a.get('href')
                url = a.get('title')
                urls.append(url)
                urls.append(urlge)
        except:
            pass

url = 'https://www.stylevana.com/en_US/promotion/flash-deals.html?dir=desc&limit=72&order=popularity&price=0-10'
urls = []
parse_link(url,urls)

print(*urls, sep="\n")
#print(*op, sep='\n')