#from urllib.request import urlopen
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup



#my_url = Request('https://www.newegg.ca/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=1080+ti&ignorear=0&N=-1&isNodeId=1', headers={'User-Agent': 'Mozilla/5.0'})
my_url = Request('https://www.newegg.ca/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=1080+ti&ignorear=0&N=-1&isNodeId=1', headers={'User-Agent': 'Mozilla/5.0'})
uClient = urllib.request.urlopen(my_url)
page_html = uClient.read()
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser")
#print(page_soup)


containers = page_soup.findAll("div", {"class":"item-container"})
#len(containers)
#containers[0]
filename = "product.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
	
	brand = containers[0].div.div.a.img["title"]
	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text
	
	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()
	
	print ("brand: " + brand)
	print ("product_name: " + product_name)
	print ("shipping: " + shipping)
	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
f.close()

#len(containers)
#containers[1]

#//*[@id="statsTotalPaid"]

  
  
 