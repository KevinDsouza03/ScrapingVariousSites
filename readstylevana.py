import requests
from bs4 import BeautifulSoup
from pastebin import PastebinAPI
 
def parse_link(linkge,array):
    reqs = requests.get(linkge)
    content = reqs.text
    soup = BeautifulSoup(content, 'html.parser')
    for h in soup.findAll('div',{"class":"product-item-details"}): #finds all products on given url, since on the site they all begin w product-item-details
        a = h.find('a') #a contains title and link
        try:
            if('title') in a.attrs:
                urlge = a.get('href')
                url = a.get('title')
                urls.append(url)
                urls.append(urlge) #write to arr for later

        except:
            pass

#url = 'https://www.stylevana.com/en_US/promotion/flash-deals.html?dir=desc&limit=72&order=popularity&price=0-10'
urls = []
#parse_link(url,urls)
url = 'https://www.stylevana.com/en_US/skincare.html?limit=72&price=3.75-10.01'
parse_link(url,urls)
parse_link(url,urls)
for x in range(2,24,1): #24 pages on the skincare s
    url_front = "https://www.stylevana.com/en_US/skincare.html?limit=72&p="
    url_back = "&price=3.75-10.01"
    url_middle = str(x+1)
    url = url_front+url_middle+url_back
    parse_link(url,urls)

#print(*urls, sep="\n")
f = open('Results.txt','w',encoding='utf-8')
for listitem in urls:
    f.write('%s\n'% listitem)
print(len(urls))