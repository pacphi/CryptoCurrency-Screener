import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask("__name__")


class Scraper:
    def __init__(self, keywords):
        self.markup = requests.get('https://economictimes.indiatimes.com/markets/cryptocurrency').text
        self.keywords = keywords

    def parse(self):
        soup = BeautifulSoup(self.markup, 'lxml')
        links = soup.findAll('a', limit=300)  
        self.news_links = []
        self.news_linksTexts = []
        for link in links:
            for keyword in self.keywords:
                if keyword in link.text and '?' not in link.text:
                    self.news_links.append(link)
        for link in self.news_links:
            self.news_linksTexts.append(link.text)



@app.route('/')
def home():
    s = Scraper([
    'cryptocurrency',
    'crypto',
    'bitcoin',
    'crash',
    'cryptocurrency prices',
    'government',
    'ranks',
    'towards',
    'crash',
    'market',
    'trends',
    'financials',
    'capitalist'
    ])

    news_list = []
    s.parse()
    for x in s.news_linksTexts:
        news_list.append(x)
    return render_template("index.html",news=list(set(news_list)))


@app.route('/table')
def table_creator():
    return render_template("table.html")


@app.route('/chart')
def chart_creator():
    return render_template("chart.html")   


if __name__=='__main__':
    app.run(debug=True)

