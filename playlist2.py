#!/usr/bin/python3

import os
import sys
from bs4 import BeautifulSoup

ALBUMS_PATH="albums/"
ARTISTS_PATH="artists/"
GENRES_PATH="genres/"
SONGS_PATH="songs/"
COVERS_PATH="covers/"

albums = []
artists = []
genres = []
songs = []
covers = []

def open_xml (file_path):
file_xml = open(file_path, "r").read()

    return BeautifulSoup(file_xml, 'xml')


def show_menu()
	while option_menu !=0: # bucle principal
	print("--- Menu ---")
	print("1. Albums")
	print("2. Artist")
	print("3. Songs")
	print("4. Genres")
	print("0. Salir")

	option_menu = input("Choose an option (0-4): ")

	if option_menu.isdigit():
	  option_menu = int(option_menu)
	  match option_menu:
	  case 0:
		print("Hata pronto")
		sys.exit()
	  case 1: 
		show_menu_albumns()
	  case 2:
		show_menu_artists()
	  case 3:
		show_menu_songs()
	  case 4:
		show_menu_genres()
	  case _:
		print("No has introducido un numero entre (0-4)")	
	else:
	  print("Hasta pronto")
	  sys.exit()

def show_albums_opts ():
	album = int (input("Choose album: "))
	print("--- Albums Options ---")
	print("1. Show songs")
	print("2. Show artist/s")
	print("3. Show cover")
	print("0. Bach")

	option_menu = input("Choose an option (0-3): ")

	match option_menu:
	  case 0:
		print("Hasta pronto")
		sys.exit()
	  case 1:
		show_album_songs(album)
	
def show_menu_songs():
	print("--- Songs Menu ---")
	print(1. "List all songs")
	print(2. "Search song by title")
	print("0. Back")

	option_menu = int(input("Choose an option (0-2): "))

	match option_menu:
	  case 1:
		pass


def show_album_songs_opt (album_id):
	print("--- Song Menu ---")	
	print("1. Play")
	print("2. Show Lyrics")
	print("0. Back")

	option_menu = int(input("Choose an option (0-2): "))
	match option_menu:
	  case 1:
		pass

def show_album_songs (album_id):
	found = false

	for album in albums:
	  if album_id != album["id"]:
		continue
	found = true
	for song in album["songs"]:
		print(song["id"]," ", song["title"])

		break
	
	if found:
	  show_album_songs_opts(album_id)
	else:
	  print("Album not found")


def show_albums()
	for album in albums:
	  print(album["id"], " ", album["tilte"])

def show_menu_albums():
	global albums

	print("--- Albums ---")
	print("1. List all albums")
	print("2. Search album by title") 
	print ("0. Back")
	option_menu = input("Choose an option (0-2): ")

	if option_menu.isdigit():
	  option_menu = int (option_menu)
	  match option_menu:
		case 0:
		  return
		case 1:
		  show_albums()
		  show_albums_opts()
		case _:
		  print("Opcion incorrecta")
		  return


def load_album (file_name):
    file_path= ALBUMS_PATH+file_name
    album_xml = open_xml(file_path)
    album = {
        "id": album_xml.album["id"],
        "title": album_xml.title.text,
      }
        return album


def load_song_num(file_name):
    file_path= SONGS_PATH+file_name
    song_xml = open_xml(file_path)

    song = {
	"id": song_xml.songs["id"],
	"title": song_xml.title.text,
	"artists": song_xml.artist
    }

def load_album_num (album_num):
    global ALBUMS_PATH

    file_name = ALBUMS_PATH+"album_"+str(album_num)+".xml"

    return load_albun(file_name)

def load_albums (album_num):
    global ALBUMS_PATH
    # Aqui estamos haciendo una concatenacion, en pyhton aunque use el tipado dinamico cuando concatenamos hay que hacer un pequeño casteo con str()

    albums_dir = os.listdir(ALBUMS_PATH)
    for album in albums_dir:
        if not album.endswith(".xml"):
            continue # Salta a la siguiente iteracion
        albums.append(load_album(album))

        print(albums)

load_albums()



# Aqui iria el ejemplos3.py
	
def load_album (file_name):
	file_path = ALBUMS_PATH+file_name
	album_xml = open_xml(file_path)
	album_songs = []

	print ("---")	
	for song in album_xml.find_all("song"):
	album_song = {
	  "id": song["id"],
	  "title": song.text
	}

	albums_songs.append(album_song)

	album = {
	  "id" : album_xml.album["id"],
	  "title" : album_xml.title.text,
	  "songs" : album_songs
	}
	
	print (album)
		
	return album


    album = {
        "id":album_xml.album['id'],
        "title": album_xml.title.text,
    }
    return album_xml

    album = {
        "id":"1",
        "title": "TITULO!",
        "cover": "IMAGEN",
        "artists": [
            {
                "id":1,
                "name":""
            },
            {
            },
            {
                ...
            }
        ]
        "songs":[
            {
                "id":1,
                "title":""
            },
            {
                "id":1,
                "title":""
            },
            {
                ...
            }
        ]

    }

    return album_xml


