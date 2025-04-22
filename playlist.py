#!/usr/bin/python3

from bs4 import BeautifulSoup

def mostrar_menu_principal():
	while True:
		print("--- Menú Principal ---")
		print("1. Ver Álbumes")
		print("2. Ver Artistas")
		print("3. Ver Canciones")
		print("4. Ver Géneros")
		print("0. Salir")

		eleccion = input("Selecciona una opción (0-4): ")

		if eleccion.isdigit():
			eleccion = int(eleccion)
			if eleccion >= 0 or eleccion <= 4:
				return eleccion
			else:
				print("Por favor, ingresa un número entre 0 y 4.")
		else:
			print("Error: Debes ingresar un número válido.")

def menu_canciones():
	print("--- Menú de Canciones ---")
	print("1. Listar todas las canciones")
	print("2. Buscar canción por título")
	print("0. Volver al menú principal")

def menu_albumes():
	print("--- Menú de Álbumes ---")
	print("1. Listar todos los álbumes")
	print("2. Buscar álbum por nombre")
	print("0. Volver al menú principal")

def menu_artistas():
	print("--- Menú de Artistas ---")
	print("1. Listar todos los artistas")
	print("2. Buscar artista por nombre")
	print("0. Volver al menú principal")

def menu_generos():
	print("--- Menú de Géneros ---")
	print("1. Listar todos los géneros")
	print("2. Buscar género por nombre")
	print("0. Volver al menú principal")
