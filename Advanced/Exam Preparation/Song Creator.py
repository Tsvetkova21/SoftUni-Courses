import os
def add_songs(*songs):
    lyrics_and_songs = {}
    for song in songs:
        new_song, lyrics = song[0], song[1]
        if new_song not in lyrics_and_songs:
            lyrics_and_songs[new_song]=[]
        lyrics_and_songs[new_song].extend(lyrics)

    result = []
    for song_title, song_lyrics in lyrics_and_songs.items():
        result.append('- ' + song_title)
        if song_lyrics:
            result.extend(song_lyrics)
    return '\n'.join(result)

print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))

