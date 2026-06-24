import requests
from bs4 import BeautifulSoup
import csv
import time
import random





page=1
while True
	url=f"https://books.toscrape.com/catalogue/{page}.html"
	HEADERS = {
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
	
	response=requests.get(url,headers=HEADERS)
	
	time.sleep(random.uniform(1,3))
	
	soup=BeautifulSoup(response.text,"html.parser")
	#tag that hold data of interest
	items=soup.find_all("article",class_="product_pod")
	
	#saving data to csv file
	with open("BOOKS.csv","w")as file:
		writer=csv.writer(file)
		writer.writerow(["title","price","rating"])
	#looping through items and extracting specific data
		for item in items:
			title=item.find("h3").text
			prices=item.find("div",class_="product_price")
			price=prices.find("p").text
			rating=item.find("p").text
			writer.writerow([title,price,rating])