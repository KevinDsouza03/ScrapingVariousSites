import functionheaders
 
#url = 'https://www.stylevana.com/en_US/promotion/flash-deals.html?dir=desc&limit=72&order=popularity&price=0-10'
urls = []
url = 'https://www.stylevana.com/en_US/promotion/trending-brands.html?dir=desc&limit=72&order=popularity&price=0-10.01'

"""
functionheaders.parse_link(url,urls)
for x in range(2,6,1):
    url_front = "https://www.stylevana.com/en_US/promotion/trending-brands.html?dir=desc&limit=72&order=popularity&p="
    url_back = "&price=0-10.01"
    url_middle = str(x+1)
    url = url_front+url_middle+url_back
    functionheaders.parse_link(url,urls)
"""
"""
url = 'https://www.stylevana.com/en_US/skincare.html?limit=72&price=3.75-10.01'
functionheaders.parse_link(url,urls)
for x in range(2,24,1): #24 pages on the skincare s
    url_front = "https://www.stylevana.com/en_US/skincare.html?limit=72&p="
    url_back = "&price=3.75-10.01"
    url_middle = str(x+1)
    url = url_front+url_middle+url_back
    functionheaders.parse_link(url,urls)
"""
url = 'https://www.pacsun.com/mens/sale/'
#functionheaders.proxy_get('ecfhgyaxz002dqdb29uefx90cf0ujy0y0qerp2cf')
functionheaders.parse_pacsun(url,urls)
print(*urls, sep="\n")
functionheaders.write_to_file('itemsResults\pacsunMensSale.txt',urls)
