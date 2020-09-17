import sys # Pentru command line arguments
import requests # Pentru a face un request de tip POST [ python -m pip install Requests ]
from bs4 import BeautifulSoup # Ne ajuta preluarea datelor [ python -m pip install BeautifulSoup4 ]

if len(sys.argv) > 1:
	idnp = sys.argv[1]
else:
	idnp = int(input('IDNP='))

parametru = {'idnp':idnp}

with requests.session() as s:
	url = "https://api.ceiti.md/date/login"
	r = s.post(url, data = parametru)

	logat = False if("IDNP format din 13 cifre" in r.text) else True
	if(not logat):
		print('IDNP-UL NU A FOST GASIT!')
		exit()

	soup = BeautifulSoup(r.content, 'html.parser')
	date_personale = soup.find(id='date-personale')
	data1 = date_personale.find_all('th')
	data2 = date_personale.find_all('td')

	for a,b in zip(data1,data2):
		print(a.get_text() + ': ' + b.get_text())