
# amend content

songs = open("readFileSample.txt", "a")
songs.write('\n "Mind Playing Tricks on Me" by Geto Boys')
songs.close()

# write new file

songs = open("readFileSample1.txt", "w")
songs.write('\n "Mind Playing Tricks on Me" by Geto Boys')
songs.close()