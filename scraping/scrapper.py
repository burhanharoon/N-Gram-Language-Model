import requests
from bs4 import BeautifulSoup
r1 = requests.get(
    'https://www.geo.tv/latest/406297-javed-miandad-induction-into-pcb-hall-of-fame')
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html.parser')
coverpage_news = soup1.select(
    '.qa-story-body.story-body.gel-pica.gel-10/12@m.gel-7/8@l.gs-u-ml0@l')
print(coverpage_news)
