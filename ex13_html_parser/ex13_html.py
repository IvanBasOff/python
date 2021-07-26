import csv
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,
                 site):
        self.site = site
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        a = []
        for tag in sp.find_all("a"):
            #print(tag)
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)
                a.append(url)
            #with open("result.csv", "w") as f:
            #    w = csv.writer(f,
            #                   delimiter = ",")
            #    for line in a:
            #        w.writerow(line)
            with open("result.txt", "w") as f:
                for line in a:
                    f.write(line + "\n")
            
        

news = "https://yandex.ru/news/?utm_source=main_stripe_big"
Scraper(news).scrape()


