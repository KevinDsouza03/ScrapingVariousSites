import csv
import requests
from bs4 import BeautifulSoup
from pastebin import PastebinAPI

#adding proxy to avoid throttling
proxies = {
    #'http': 'http://dmtfibkh:ti0pow5ehwg4@170.244.93.158:7719/'
}

""" attempted to use an object here but proved very difficult to put delimiter btwn object vars. come back later
class parsed_data:
    def __init__(self,title,link,price):
        self.title = title
        self.link = link
        self.price = price
    def __str__(self):
        return f"{self.link}{self.title}{self.price}"

    def __iter(self):
        return iter([self.title,",",self.price,",",self.link])
 """
def parse_link(linkge,array): 
    
    reqs = requests.post(linkge,proxies=proxies)
    reqs = requests.get(linkge)
    content = reqs.text
    soup = BeautifulSoup(content, 'html.parser')
    for h in soup.findAll('div',{"class":"product-item-details"}): #finds all products on given url, since on the site they all begin w product-item-details
        a = h.find('a') #a contains title and link
        try:
            if('title') in a.attrs:
                #temp = parsed_data(a.get('href'),a.get('title'), 5)
                #array.append(temp)
                # ^remnants of object attempt
                array.append(a.get('title'))
                array.append(a.get('href'))
        except:
            pass
        

def write_to_txt(path,array_to_write_from):
    f = open(path,'w',encoding='utf-8')
    for listitem in array_to_write_from:
        f.write('%s\n' % listitem)

def write_to_csv(path,array_to_write_from,headers):
    f = open(path,'w',newline='',encoding='utf-8')
    writer = csv.writer(f,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)
    writer.writerow(array_to_write_from)