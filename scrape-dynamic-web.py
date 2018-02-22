from bs4 import BeautifulSoup
import requests
#from selenium import webdriver

url = "https://zclassic.miningspeed.com/workers/t1VGp7pNxjiueRRaS3wXRee5wjkmGc7EjAN"
web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, 'html.parser')
total=0
tables = web_soup.find_all('table')
#print(tables[2])
for row in tables[2].find_all('tr'):
    for td in row.find_all('td'):
        for a in td.find_all('a'):
            split = (a.text).split(' ')
            total = total + float(split[0])
            
    
            
print("Rig 2: " + str(round(total,8)) + " ZCL")
url = "https://zclassic.miningspeed.com/workers/t1KTHToeHPrEhCa5E51WoFHG5theoBjeJuN"
web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, 'html.parser')
total2=0
tables = web_soup.find_all('table')
#print(tables[2])
for row in tables[2].find_all('tr'):
    for td in row.find_all('td'):
        for a in td.find_all('a'):
            split = (a.text).split(' ')
            total2 = total2 + float(split[0])
print("Pineapple Express: " + str(round(total2,8)) + " ZCL")


print("Total: " + str(round(total2+total,8)) + " ZCL")


#v#id_id = vid_src.split('/')[4]

#for article in web_soup.findAll('table', {"class":"table striped responsive-table table-hover"}):
	#headline = article.tr[1].td[2].a.text
#	print(article)
	#page_soup.findAll("div", {"class":"item-container"})
#	summary = article.p.text
#	print(summary)
#/html/body/main/div/div[2]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]/a
#<a href="http://zclassicexplorer.com/tx/f13c1ecb778a748a5d0824ead3595b5dcebe118cd92093229bf6d43a0302db61" target="_blank">0.0186701 ZCL</a>
#article = web_soup.find('div', class_='tab-pane fade')
#print(article.tr)

#/html/body/main/div/div[2]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]/a

#headline = article.h2.a.text

#for title_container in web_soup.findAll("div",{"id":"Payments"}):
 #   print(title_container[4].a.text)
	


#find('div', class_='entry-content')


#driver = webdriver.Firefox()
#driver.get(url)
#html = driver.execute_script("return document.documentElement.outerHTML")
#sel_soup = BeautifulSoup(html, 'html.parser')
#print(sel_soup)
#title_containers = sel_soup.findAll("span",{"id":"statsTotalPaid"})
#print(title_containers[0].text)


#print(len(sel_soup.findAll("img")))

#images = []

#for i in sel_soup.findAll("img"):
#    print(i)
#    #print(dir(i))
#    src = i["src"]
#    images.append["src"]

#print(images)


