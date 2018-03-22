from youtube_dl import YoutubeDL

#download 1 song:
'''song = YoutubeDL()
song.download(['https://www.youtube.com/watch?v=i7UM4AcDzE8'])
'''

#download many song:
'''song = YoutubeDL()
song.download(['https://www.youtube.com/watch?v=8TeK2H9RO70',
'https://www.youtube.com/watch?v=xLYN94jkiDo',
'https://www.youtube.com/watch?v=iQBYrTjtBOE'])
'''

#download audio:
'''opitions = {
    'format' : 'bestaudio/audio'
}
song = YoutubeDL(opitions)
song.download(['https://www.youtube.com/watch?v=TJjvqQBqG2o'])
'''
#search and download video:
'''opitions = {
    'default_search' : 'ytsearch',
    'max_download' : 1
}
song = YoutubeDL(opitions)
song.download(['Con điên tamka pkl'])
'''

#search and download audio:
'''opitions = {
    'default_search' : 'ytsearch',
    'max_download' : 1,
    'format' : 'bestaudio/audio'
}
song = YoutubeDL(opitions)
song.download(['MINE Bazzi'])
'''
