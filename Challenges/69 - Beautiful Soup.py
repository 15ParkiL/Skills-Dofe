from bs4 import BeautifulSoup
import urllib2

resp = urllib2.urlopen("http://www.gpsbasecamp.com/national-parks")
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))

for link in soup.find_all('a', href=True):
    print(link['href'])
