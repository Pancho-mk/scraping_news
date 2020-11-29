#!/usr/bin/env python
# Scraping news from a website and writing the headlines and the links in a csv file.
# Opens that file for reading
import requests
from bs4 import BeautifulSoup
import csv
import os
from subprocess import Popen, PIPE

r = requests.get('https://www.kurir.mk')
#print(type(res))

soup = BeautifulSoup(r.text, 'lxml')
najnovi_vesti = soup.find('div', class_='najnovi-vesti')

print('Working...')

csv_file = open('kurir.csv', 'w')
csv_writer = csv.writer(csv_file)   
csv_writer.writerow(['headline', 'summary'])
#print(najnovi_vesti.prettify())
linkovi = najnovi_vesti.find_all('a', class_='article-link')
for link in linkovi:
	art_text2 = link.h3.text.strip()
	art_text = art_text2.split('  ')[0]
	art_link = link.get('href')
	csv_writer.writerow([art_text, art_link])
	print(art_text)
	print(art_link)

csv_file.close()

process = subprocess.Popen(['xdg-open', 'kurir.csv'])




