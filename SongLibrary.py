import Classes

print("""

***************************
Welcome To The Song Library
***************************

Operations

1. Show Songs
2. Search Song
3. Add Song
4. Remove Song
5. Total Listening Time

To exit press "q"

""")

song_library = Classes.SongLibrary()
song_library.connect()

while True:

    operation = input("Enter the number of the operation: ")

    if operation == "q":
        print("Thank you for visiting the song library.")
        song_library.disconnect()
        break

    elif operation == "1":
        print("Songs in the library\n")
        song_library.showSongs()

    elif operation == "2":
        song_name = input("Name of the song: ")
        song_library.showSong(song_name)

    elif operation == "3":
        name = input("Track Name: ")
        artist = input("Artist: ")
        album = input("Album: ")
        producer = input("Producer: ")
        length = int(input("Length(seconds): "))

        song = Classes.Song(name,artist,album,producer,length)
        print( "\n" )
        print(song)
        song_library.addSong(song)
        print( "\n" )

    elif operation == "4":
        song_name = input( "Name of the song: " )
        song_library.deleteSong(song_name)

    elif operation == "5":
        song_library.totalLength()


