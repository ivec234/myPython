from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.tangerine.ca/app/#/accounts/credit_card/31323334353637383930313233343536b2e8fb47ac2f50e11b1cdd1a7c79d854ebe4a8306ee28bf931cfdd7bbaa6d5a4').text
soup = BeautifulSoup(source,'lxml')
print(soup)
#csv_file = open('cms_scrape.csv','w')
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['Headline', 'Summary','Video_link'])

#for article in soup.find_all('article'):

