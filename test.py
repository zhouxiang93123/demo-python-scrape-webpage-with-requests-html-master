
from requests_html import HTMLSession
session = HTMLSession()
url = 'https://www.bbc.co.uk/programmes/w3csvqp7'
r = session.get(url)
sel = '#orb-modules > div > div > div:nth-child(2) > div.b-g-p.no-margin-vertical > div > div.grid> div > div.island > div.grid-wrapper > div.grid> div > div.map__intro__synopsis.centi '
results = r.html.find(sel)
results[0].text
print('\n' + results[0].text)
