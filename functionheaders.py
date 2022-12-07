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
                array.append(url)
                array.append(urlge) #write to arr for later

        except:
            pass

def write_to_file(path,array_to_write_from):
    f = open(path,'w',encoding='utf-8')
    for listitem in array_to_write_from:
        f.write('%s\n' % listitem)
    print(len(array_to_write_from))