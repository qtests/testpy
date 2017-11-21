# Test scraping

# https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20170821&end=20171121
# http://urllib3.readthedocs.io/en/latest/user-guide.html

import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20170821&end=20171121"  # change to whatever your url is

response = http.request('GET', url)
soup = BeautifulSoup(response.data.decode('utf-8'))

# for tr in soup.find_all('tr')[1:]:
#     tds = tr.find_all('td')
#     print ("Date: %s; Open: %s; High: %s; Low: %s; Close: %s; Volume: %s; MCap: %s" % \
#             (tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text))

with open('output.txt', 'w') as f:
    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        f.write("Date: %s; Open: %s; High: %s; Low: %s; Close: %s; Volume: %s; MCap: %s\n" % \
             (tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text))

print ("__Finito__")