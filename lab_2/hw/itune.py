from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel
url = 'https://www.apple.com/itunes/charts/songs/'

html_content = urlopen(url).read().decode('utf8')

Soup = BeautifulSoup(html_content, 'html.parser')



section = Soup.find('section', 'section chart-grid' )

li_list = section.find_all('li')
#save into xls file
songs = []
for li in li_list:
    song = {}
    song['name'] = li.h3.string
    song['artist'] = li.h4.string
    songs.append(song)
pyexcel.save_as(records= songs, dest_file_name= 'top_song.xls')

# search and download on youtube:

opitions = {
    'default_search' : 'ytsearch',
    'max_download' : 1
}

download_song = YoutubeDL(opitions)

for li in li_list:
    song_name = li.h3.string
    song_artist = li.h4.string
download_song.download(song_name + song_artist)    
