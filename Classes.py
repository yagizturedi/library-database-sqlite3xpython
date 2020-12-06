import sqlite3

## Library Classes

class Book():
    def __init__(self,name,author,publisher,genre,edition):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.edition = edition

    def __str__(self):
        return "Book Name: {}\nAuthor: {}\nPublisher: {}\nGenre: {}\nEdition: {}\n".format(self.name,self.author,self.publisher,self.genre,self.edition)

class Library():
    def __init__(self):
        self.connect()

    def connect(self):
        self.connection = sqlite3.connect( "Library.db" )
        self.cursor = self.connection.cursor()

        create_table = "CREATE TABLE IF NOT EXISTS BOOKS (BOOK_NAME TEXT, AUTHOR TEXT, PUBLISHER TEXT, GENRE TEXT, EDITION INT)"

        self.cursor.execute(create_table)
        self.connection.commit()

    def disconnect(self):
        self.connection.close()

    def showBooks(self):

        query = "SELECT * FROM BOOKS"

        self.cursor.execute(query)
        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There are no books in the library yet.")

        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4])
                print(book)

    def queryBook(self,name):
        query = "SELECT * FROM BOOKS WHERE BOOK_NAME = ?"
        self.cursor.execute(query,(name,))
        books = self.cursor.fetchall()

        if len( books ) == 0:
            print( "There are no books in the library as queried." )

        else:
            for i in books:
                book = Book( i[0], i[1], i[2], i[3], i[4] )
                print( book )

    def addBook(self,book):

        query= "INSERT INTO BOOKS VALUES(?,?,?,?,?)"

        self.cursor.execute(query,(book.name,book.author,book.publisher,book.genre,book.edition))
        self.connection.commit()

    def removeBook(self,book_name):
        query = "DELETE FROM BOOKS WHERE BOOK_NAME = ?"

        self.cursor.execute(query,(book_name,))
        self.connection.commit()

    def updateEdition(self,book_name):
        query = "UPDATE BOOKS SET EDITION = EDITION+1 WHERE BOOK_NAME = ?"

        self.cursor.execute(query,(book_name,))

        self.queryBook(book_name)


## Song Library Classes
class Song:
    def __init__(self, name, artist, album, producer, length):
        self.name = name
        self.artist = artist
        self.album = album
        self.producer = producer
        self.length = length

    def __str__(self):
        return "Name: {}\nArtist: {}\nAlbum: {}\nProducer: {}\nLength: {}".format( self.name, self.artist, self.album,
                                                                                 self.producer, str(self.length) )


class SongLibrary:
    def __init__(self):
        self.connect()

    def connect(self):

        self.connection = sqlite3.connect("library.db")
        self.cursor = self.connection.cursor()

        create_table = "CREATE TABLE IF NOT EXISTS SONGS (SONG_NAME TEXT, " \
                       "ARTIST TEXT, ALBUM TEXT, PRODUCER TEXT, LENGTH INT)"

        self.cursor.execute(create_table)
        self.connection.commit()

    def disconnect(self):
        self.connection.close()

    def showSongs(self):

        query = "SELECT * FROM SONGS"

        self.cursor.execute(query)
        songs = self.cursor.fetchall()

        if len(songs) == 0:
            print("There are no songs in the library yet.")

        else:
            print("Songs in the library: \n")
            for song in songs:
                queried_song = Song(song[0],song[1],song[2],song[3],song[4])
                print(queried_song)
                print("\n")

    def showSong(self,song_name):

        query = "SELECT * FROM SONGS WHERE SONG_NAME = ?"

        self.cursor.execute( query ,(song_name,))
        songs = self.cursor.fetchall()

        if len( songs ) == 0:
            print( "There are no songs in the library fitting the query." )

        else:
            print( "Songs in the library: \n" )

            for song in songs:
                queried_song = Song( song[0], song[1], song[2], song[3], song[4] )
                print( queried_song )
                print( "\n" )

    def deleteSong(self,song_name):

        query = "DELETE FROM SONGS WHERE SONG_NAME = ?"

        self.cursor.execute(query,(song_name,))
        self.connection.commit()

        print("Song(s) are deleted successfully.")

    def addSong(self,song):
        query = "INSERT INTO SONGS VALUES(?,?,?,?,?)"

        self.cursor.execute(query,(song.name,song.artist,song.album,song.producer,song.length))
        self.connection.commit()

    def totalLength(self): ## NOT COMPLETED YET

        query = "SELECT SUM(LENGTH) FROM SONGS"

        self.cursor.execute(query)
        print("Total length of songs in the library: {} seconds".format(self.cursor.fetchall()[0][0]))

