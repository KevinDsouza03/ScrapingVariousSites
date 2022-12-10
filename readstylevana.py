import functionheaders
import time
#url = 'https://www.stylevana.com/en_US/promotion/flash-deals.html?dir=desc&limit=72&order=popularity&price=0-10'
urls = []
url = 'https://www.stylevana.com/en_US/promotion/trending-brands.html?dir=desc&limit=72&order=popularity&price=0-10.01'
header_list = ['Title','Original Price','Link']
"""
functionheaders.parse_link(url,urls)
for x in range(2,6,1):
    url_front = "https://www.stylevana.com/en_US/promotion/trending-brands.html?dir=desc&limit=72&order=popularity&p="
    url_back = "&price=0-10.01"
    url_middle = str(x+1)
    url = url_front+url_middle+url_back
    functionheaders.parse_link(url,urls)
"""
start_time = time.time()
url = 'https://www.stylevana.com/en_US/skincare.html?limit=72&price=3.75-10.01'

functionheaders.parse_link(url,urls)
for x in range(2,24,1): #24 pages on the skincare 
    url_front = "https://www.stylevana.com/en_US/skincare.html?limit=72&p="
    url_back = "&price=3.75-10.01"
    url_middle = str(x+1)
    url = url_front+url_middle+url_back
    functionheaders.parse_link(url,urls)

end_time = time.time()
elapsed_time = end_time-start_time

print (f"Time to parse: {elapsed_time}")
print(len(urls))
#print(*urls, sep="\n")
start_time = time.time()
functionheaders.write_to_csv('itemsResults\skincareResults.csv',urls,header_list)
end_time = time.time()
elapsed_time = end_time-start_time
print (f"Time to write: {elapsed_time}")
