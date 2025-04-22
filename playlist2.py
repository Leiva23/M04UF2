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

def load_album (file_name):
    file_path= ALBUMS_PATH+file_name
    album_xml = open_xml(file_path)
    album = {
        "id": album_xml.album["id"],
        "title": album_xml.title.text,
      }
        return album

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

laod_albums()

    album = {
        "id":album_xml.añbum['id'],
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


