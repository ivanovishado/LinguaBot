# coding: utf-8

from bs4 import BeautifulSoup
import requests
import re
import urllib.request, urllib.error, urllib.parse
import os
import http.cookiejar
import json


def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')


query = input("Query: ")# you can change the query for the image  here
image_type="ActiOn"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print(url)
#add the directory for your image here
DIR="Pictures"
header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}
soup = get_soup(url, header)

ActualImages = []  # contains the link for Large original images, type of  image

for a in soup.find_all("div", {"class": "rg_meta"}):
    link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
    ActualImages.append((link, Type))

print("there are total", len(ActualImages), "images")

if not os.path.exists(DIR):
    os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
    os.mkdir(DIR)

f = open("links.txt", "w")
for i, (img, Type) in enumerate(ActualImages):
    try:
        req = urllib.request.Request(img, headers={'User-Agent': header})
        raw_img = urllib.request.urlopen(req).read()

        f.write(link)

        #cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        #print(cntr)
        '''if len(Type) == 0:
            f = open(os.path.join(DIR, image_type + "_" + str(cntr) + ".jpg"), 'wb')
        else:
            f = open(os.path.join(DIR, image_type + "_" + str(cntr) + "." + Type), 'wb')

        f.write(raw_img)
        f.close()'''
    except Exception as e:
        #print("could not load : " + img)
        #print(e)
        pass
