import requests
from bs4 import BeautifulSoup


class internetBanking:

    url = ''

    def setURL(self, url):
        self.url = url

    def checkConnection(self):
        try:
            r = requests.get(self.url)
            r.raise_for_status()
            return True
        except requests.exceptions.RequestException:
            return False
