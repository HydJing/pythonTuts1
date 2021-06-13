
songs = open("readFileSample.txt", "r")

for song in songs.readlines():
    print(song)

songs.close()
