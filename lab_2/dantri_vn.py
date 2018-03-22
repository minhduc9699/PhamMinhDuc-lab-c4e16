from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'http://dantri.com.vn'
#1. download web

html_content = urlopen(url).read().decode('utf8')

#1.1 save html_content
#luw 1 lan
'''html_file = open('dantri.html', 'wb')
html_file.write(html_content)
html_file.close()'''


#2. extract ROI
Soup = BeautifulSoup(html_content, "html.parser") #xml, #xhtml, #html

#print(Soup.prettify())
ul = Soup.find('ul', 'ul1 ulnew')
#print(ul.prettify())


#3. extract info
list_of_news = []
li_list = ul.find_all('li')
for li in li_list:
    dict_of_news= {}
    a = li.h4.a #tim tag tu tren xuong duoi
    news = a.string
    link = url + a['href']
    dict_of_news['news'] = news
    dict_of_news['link'] = link
    list_of_news.append(dict_of_news)
pyexcel.save_as(records=list_of_news, dest_file_name= 'news.xls')
