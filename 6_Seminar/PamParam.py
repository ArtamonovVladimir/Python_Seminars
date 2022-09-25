path = "6_Seminar\song_in.txt"
with open(path, 'r') as text:
    in_data = text.read()
song = in_data.split(' ')
print(song)


def check_song(song):
    counts = 0
    y = song[0].count('a')
    for i in song:
        x = i.count('a')
        if x == y:
            counts += 1

    return counts


print(check_song(song))
# result = bool(lambda x: True if check_song(song)==len(song) else False)

print('Парам-пам-пам' if check_song(song) == len(song) else 'Пам парам')
