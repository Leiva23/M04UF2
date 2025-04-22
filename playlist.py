#!/usr/bin/python3

from bs4 import BeautifulSoup

def show_menu():
	while True:
		print("--- Menu ---")
		print("1. Albums")
		print("2. Artists")
		print("3. Songs")
		print("4. Genres")
		print("0. Exit")

		option_menu = input("Choose an option (0-4): ")

		if option_menu.isdigit():
			option_menu = int(option_menu)
			if 0 <= option_menu <= 4:
				return option_menu
			else:
				print("Please, enter a number between 0 and 4.")
		else:
			print("Error: You must enter a valid number.")

def show_menu_songs():
	print("--- Songs Menu ---")
	print("1. List all songs")
	print("2. Search song by title")
	print("0. Return")

def show_menu_albums():
	print("--- Albums Menu ---")
	print("1. List all albums")
	print("2. Search album by title")
	print("0. Return")

def show_menu_artists():
	print("--- Artists Menu ---")
	print("1. List all artists")
	print("2. Search artist by title")
	print("0. Return")

def show_menu_genres():
	print("--- Genres Menu ---")
	print("1. List all genres")
	print("2. List genre by title")
	print("0. Return")

version = 0.5

app_title="Playlist v" + str(version)

print(app_title)
print("-" * len(app_title))

#xml_ejemplo = '<personaje><nombre>Jacinto</nombre><edad valor="33" /></personaje>'

#print(xml_ejemplo)

#personaje = BeautifulSoup(xml_ejemplo, 'xml')

#print(personaje.prettify())

#nombre = personaje.nombre

#print(nombre.contents)
#print(nombre.text)

song_xml = open("songs/song_1.xml", "r").read()

#print(song_xml)

song = BeautifulSoup(song_xml, 'xml')

print(song.title.text)
print(int(song.duration["seconds"])/60)

print(song.artists.find("artist"))

for artist in song.artists.find("artist"):
    print(artist.text)


option_menu = show_menu()
print("You chose the option:", option_menu)

show_menu_songs()

show_menu_albums()

show_menu_artists()

show_menu_genres()
