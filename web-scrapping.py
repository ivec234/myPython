from bs4 import BeautifulSoup
import requests
import csv

#with open ('simple.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')
csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary','video_link'])
#print(soup.prettify())

match = soup.title.text
#match=soup.div
#match=soup.find('div')
#match=soup.find('div', class_='footer')

print(match)

#/////////////
article = soup.find('div', class_='article')
print(article)

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)

//////////////////////////////
for article in soup.find_all('div', class_='article')
	headline = article.h2.a.text
	print(headline)
	
	summary = article.p.text
	print(summary)
	
	
//////////////////////////////////////////


source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
#print (soup.prettify())

article = soup.find('article')
#print(article.prettify)

headline = article.h2.a.text
print(headline)

summary = article.find('div', class_='entry-content').p.title
print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']
print(sid_src)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
print(vid_id)

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(vy_link)



try:
	vid_src = article.find('iframe', class_='youtube-player')['src']
print(sid_src)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
yt_link = f'https://youtube.com/watch?v={vid_id}'


csv.writer.writerow([Headline, summary, yt_link])

csv.file.close()
