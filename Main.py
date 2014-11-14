import requests
from bs4 import BeautifulSoup
import time
import urllib.request

def avicusFaceSpider(pages):
    page = 0
    nameSave = 'logsAvic/names/names.txt'
    nameNum = 'logsAvic/names/namesNumbered.txt'
    names = open(nameSave, 'w')
    nameNumbered = open(nameNum, 'w')
    y = 1
    while page < pages:

        html = open('logsAvic/htmlsource/'+str(page), 'w')
        toCrawl = 'http://avicus.net/stats?page='+str(page+1)+'&time=overall'
        pageSource = requests.get(toCrawl)
        pageSourcePlain = pageSource.text
        soupObject = BeautifulSoup(pageSourcePlain)
        html.write(pageSourcePlain)
        time.sleep(3)
        for link in soupObject.findAll('img', {'class': 'img-rounded'}):
            image = link.get('src')
            image = image.replace('37', '128')
            nameExtended = image.replace("http://cravatar.eu/helmavatar/", "")
            namePlain = nameExtended.replace("/128.png", "")
            print(str(y) + " " + nameExtended)
            urllib.request.urlretrieve(image, "logsAvic/faces/" + namePlain + ".png")
            names.write(namePlain + "\n")
            nameNumbered.write(str(y) + " " + namePlain + "\n")
            y+=1


        page += 1

avicusFaceSpider(1000)
