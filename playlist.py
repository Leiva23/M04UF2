#!/usr/bin/python3

import os
import sys
from bs4 import BeautifulSoup

ALBUMS_PATH = "albums/"
ARTISTS_PATH = "artists/"
GENRES_PATH = "genres/"
SONGS_PATH = "songs/"

albums = []
artists = []
genres = []
songs = []

def open_xml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file_xml = f.read()
    return BeautifulSoup(file_xml, 'xml')

def load_albums():
    global albums
    albums = []
    for file_name in os.listdir(ALBUMS_PATH):
        if file_name.endswith(".xml"):
            albums.append(load_album(file_name))

def load_album(file_name):
    file_path = ALBUMS_PATH + file_name
    album_xml = open_xml(file_path)
    
    album_songs = []
    for song_tag in album_xml.find_all("song"):
        album_song = {
            "id": song_tag.get("id", ""),
            "title": song_tag.text.strip()
        }
        album_songs.append(album_song)

    album = {
        "id": album_xml.album.get("id", ""),
        "title": album_xml.title.text.strip() if album_xml.title else "Desconocido",
        "songs": album_songs,
        "artists": []
    }

    # Ya no cargamos portadas ni rutas

    return album

def load_songs():
    global songs
    songs = []
    for file_name in os.listdir(SONGS_PATH):
        if file_name.endswith(".xml"):
            songs.append(load_song(file_name))

def load_song(file_name):
    file_path = SONGS_PATH + file_name
    song_xml = open_xml(file_path)

    song_tag = song_xml.find("song")
    if song_tag is None:
        song_tag = song_xml

    song_id = song_tag.get("id", "desconocido")

    artists_list = []
    for artist in song_tag.find_all("artist"):
        artists_list.append({
            "id": artist.get("id", ""),
            "name": artist.text.strip()
        })

    genres_list = []
    for genre in song_tag.find_all("genre"):
        genres_list.append({
            "id": genre.get("id", ""),
        })

    lyrics = song_tag.lyrics.text.strip() if song_tag.lyrics else ""

    song = {
        "id": song_id,
        "title": song_tag.title.text.strip() if song_tag.title else "Desconocida",
        "artists": artists_list,
        "genres": genres_list,
        "duration_seconds": song_tag.duration.get("seconds", "") if song_tag.duration else "",
        "lyrics": lyrics
    }
    return song

def load_artists():
    global artists
    artists = []
    for file_name in os.listdir(ARTISTS_PATH):
        if file_name.endswith(".xml"):
            artists.append(load_artist(file_name))

def load_artist(file_name):
    file_path = ARTISTS_PATH + file_name
    artist_xml = open_xml(file_path)
    artist_tag = artist_xml.find("artist")
    artist = {
        "id": artist_tag.get("id", ""),
        "name": artist_tag.text.strip() if artist_tag else "Desconocido"
    }
    return artist

def load_genres():
    global genres
    genres = []
    for file_name in os.listdir(GENRES_PATH):
        if file_name.endswith(".xml"):
            genres.append(load_genre(file_name))

def load_genre(file_name):
    file_path = GENRES_PATH + file_name
    genre_xml = open_xml(file_path)
    genre_tag = genre_xml.find("genre")
    genre = {
        "id": genre_tag.get("id", ""),
        "name": genre_tag.text.strip() if genre_tag else "Desconocido"
    }
    return genre

def show_menu():
    opcion_menu = -1
    while opcion_menu != 0:
        print("\n--- Menú ---")
        print("1. Álbumes")
        print("2. Artistas")
        print("3. Canciones")
        print("4. Géneros")
        print("0. Salir")

        opcion = input("Elige una opción (0-4): ")
        if not opcion.isdigit():
            print("Por favor, introduce un número válido.")
            continue
        opcion_menu = int(opcion)

        if opcion_menu == 0:
            print("¡Hasta pronto!")
            sys.exit()
        elif opcion_menu == 1:
            show_menu_albums()
        elif opcion_menu == 2:
            show_menu_artists()
        elif opcion_menu == 3:
            show_menu_songs()
        elif opcion_menu == 4:
            show_menu_genres()
        else:
            print("No has introducido un número entre 0 y 4.")

def show_menu_albums():
    print("\n--- Álbumes ---")
    print("1. Listar todos los álbumes")
    print("2. Buscar álbum por título")
    print("0. Volver")

    opcion = input("Elige una opción (0-2): ")
    if not opcion.isdigit():
        print("Opción inválida.")
        return
    opcion = int(opcion)
    if opcion == 0:
        return
    elif opcion == 1:
        show_albums()
        show_album_options()
    elif opcion == 2:
        titulo = input("Introduce el título del álbum a buscar: ").lower()
        filtrados = [alb for alb in albums if titulo in alb["title"].lower()]
        if not filtrados:
            print("No se encontró ningún álbum con ese título.")
        else:
            for alb in filtrados:
                print(f"{alb['id']} - {alb['title']}")
            show_album_options()
    else:
        print("Opción incorrecta.")

def show_albums():
    print("\nLista de álbumes:")
    for album in albums:
        print(f"{album['id']} - {album['title']}")

def show_album_options():
    album_id = input("Elige el id del álbum: ")
    album = next((a for a in albums if a["id"] == album_id), None)
    if not album:
        print("Álbum no encontrado.")
        return

    while True:
        print(f"\n--- Opciones para el álbum '{album['title']}' ---")
        print("1. Mostrar canciones")
        print("2. Mostrar artistas")
        print("3. Mostrar portada")
        print("0. Volver")

        eleccion = input("Elige una opción (0-3): ")
        if eleccion == "0":
            break
        elif eleccion == "1":
            if album["songs"]:
                print("Canciones del álbum:")
                for song in album["songs"]:
                    print(f"{song['id']} - {song['title']}")
            else:
                print("Este álbum no tiene canciones cargadas.")
        elif eleccion == "2":
            if album["artists"]:
                print("Artistas del álbum:")
                for artist in album["artists"]:
                    print(f"{artist['id']} - {artist['name']}")
            else:
                print("No hay artistas asociados a este álbum.")
        elif eleccion == "3":
            print("No hay portadas disponibles.")
        else:
            print("Opción incorrecta.")

def show_menu_artists():
    print("\n--- Artistas ---")
    for artist in artists:
        print(f"{artist['id']} - {artist['name']}")
    input("Presiona Enter para volver...")

def show_menu_songs():
    print("\n--- Canciones ---")
    print("1. Listar todas las canciones")
    print("2. Buscar canción por título")
    print("0. Volver")

    opcion = input("Elige una opción (0-2): ")
    if not opcion.isdigit():
        print("Opción inválida.")
        return
    opcion = int(opcion)
    if opcion == 0:
        return
    elif opcion == 1:
        show_songs()
    elif opcion == 2:
        titulo = input("Introduce el título de la canción a buscar: ").lower()
        filtrados = [s for s in songs if titulo in s["title"].lower()]
        if not filtrados:
            print("No se encontró ninguna canción con ese título.")
        else:
            for s in filtrados:
                print(f"{s['id']} - {s['title']}")
    else:
        print("Opción incorrecta.")

def show_songs():
    print("\nLista de canciones:")
    for song in songs:
        print(f"{song['id']} - {song['title']}")
    input("Presiona Enter para volver...")

def show_menu_genres():
    print("\n--- Géneros ---")
    for genre in genres:
        print(f"{genre['id']} - {genre['name']}")
    input("Presiona Enter para volver...")

def main():
    load_albums()
    load_artists()
    load_genres()
    load_songs()
    show_menu()

main()
