import mechanize
import requests
from bs4 import BeautifulSoup as bs

class Util():
    def __init__(self, url, username, password):
        self.url = url
        self.data = {
            'username': username,
            'password': password
        }
        self.br = mechanize.Browser()
        self.soup = bs(requests.get(url).content, 'html5lib')

    def getUrl(self):
        return self.url

    def getBrowser():
        return self.br

    def openSite(self, url):
        self.br.open(url)
        self.soup = bs(self.br.response().read(), 'html5lib')

    def getSoup(self):
        return self.soup

    def login(self):
        url = ""
        soup = self.getSoup()
        for link in soup.find_all('a'):
            if link.text.lower() == "login":
                url = link.get('href')

        self.openSite(url)
        self.br.select_form(nr=0)
        self.br.form['username'] = self.data['username']
        self.br.form['password'] = self.data['password']
        self.br.submit()
        self.url = self.br.geturl()
        self.soup = bs(self.br.response().read(), 'html5lib')

    def find(self, sen):
        count = 0
        for letter in sen:
            if letter == "<":
                break
            count += 1
        return count

    def clean(self, contents):
        return [content.replace(content[self.find(content):], '').strip() for content in contents]
