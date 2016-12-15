import csv
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
soup = BeautifulSoup(urlopen('https://apps.wigan.gov.uk/tenders/'))

table = soup.findAll('table', attrs={ "class" : "table-horizontal-line"})

print table