#!/usr/bin/python 
#coding: utf-8 -*-
import json
import ssl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
# For ignoring SSL certificate errors
ctx ss1.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ss1.CERT_NONE
#Take a Flipkart Product URL as Input from user 
url = input('https://www.flipkart.com/samsung-t7-1-tb-external-solid-state-drive-ssd/p/itmd533336b46fa3?pid=ACCFTZGRJ7AG6ZJB&lid=LSTACCFTZGRJ7AG6ZJBVBWSUD&marketplace=FLIPKART&store=6bo&srno=b_1_1&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_4_L1_view-all&fm=organic&iid=en_h08sDCghvmnM9b1TaVN5Y5YRF%2F%2FHUFpcwAINVaic7NgBK94pKd2W7P%2Bpg%2BSDxYqVNrfoaM6hmqtcNp3HnZDQSA%3D%3D&ppt=browse&ppn=browse&ssid=ydhd7haamo0000001679645578716')
#Making the website believe that you are accessing it using a mozilla browser.
req = Request (url, headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
webpage = urlopen(req).read()
# Creating a BeautifulSoup object of the html page for easy extraction of data.
soup = BeautifulSoup (webpage, 'html.parser') 
html_obj = soup.prettify('utf-8')

#Creating a dictionary to store the different data-points that we will extract, 
product_details = {}
product_details["highlights"] = []
product_details["product_description"] = {}

#Extract average ratings, name, number of reviews, brand and image of product.
for script in soup.findAll('script', attrs={'id': 'jsonLD'}):
json_data = json.loads(script.text)
    product_details["rating"] = json_data[0]["aggregateRating"]["ratingValue"]
    product_details["no_of_reviewers"] = json_data[0]["aggregateRating"]["reviewCount"]
    product_details["brand"] = json_data[0]["brand"]["name"]
    product_details["name"] = json_data[0]["name"]
    product_details["image"] = json_data[0]["image"]
    break
#Extract top highlights of the product.
for li in soup.findAll('li', attrs={'class': '_2-riNZ'}):
    product_details["highlights"].append(li.text.strip())
#Extract the price of the product.
for div in soup.findAll('div', attrs={'class': '_1vC40E _3q09m1'}): 
    product_details["price_in_rupees"] = float(div.text.strip()[1:].replace(", ",""))
    break
#Extract key value pairs in description of the product.
description_headers = soup.findAll('div', attrs={'class': '_2THX53'})
descriptions = soup.findAll('div', attrs={'class': '_laK10F'})

for i, description in enumerate(descriptions): product_details["product_description"] [description_headers[i].text.strip()] \\
- description.text.strip()
#Save product dictionary to JSON file.
with open('product_details.json', 'w', encoding="utf-8") as outfile: 
    json.dump(product_details, outfile, indent, sort_keys=True)
#Save product HTML content to a HTML file.
with open('output_file.html', 'wb') as file: 
    file.write(html_obj)
print("--------Extraction of data is complete. Check json file.")
