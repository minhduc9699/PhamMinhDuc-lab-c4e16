from youtube_dl import YoutubeDL

song_name = input('enter name of the song you want to download: ')
song_type = input('you want download MV or Audio? (M/A): ').upper()

opitions_M = {
    'default_search' : 'ytsearch',
    'max_download' : 1
}

opitions_A = {
    'default_search' : 'ytsearch',
    'max_download' : 1,
    'format' : 'bestaudio/audio'
}


if song_type == 'A':
    song = YoutubeDL(opitions_A)
    song.download([song_name])
elif song_type == 'M':
    song = YoutubeDL(opitions_M)
    song.download([song_name])
else:
    print('not found format of song')
