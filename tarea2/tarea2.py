import requests
import json
import time

pokeapi_url = "https://pokeapi.co/api/v2/generation/"


def menu():
    selection = 0
    while selection != 6:
        print("Bienvenidos a la aplicacion de consultas sobre los pokemons")
        print("POKE-CONSULTAS v1.0")
        print("Elija una de las opciones")
        print("-"*30)
        print("1.- Pokemons por generaciones")
        print("2.- Pokemons por forma")
        print("3.- Pokemons por habilidad")
        print("4.- Pokemons por habitad")
        print("5.- Pokemons por tipo")
        print("6.- Salir")
        selection = int(input("\n Elija una opción: "))
        if selection == 1:
            poke_generation()
        elif selection == 2:
            poke_form()
        elif selection == 3:
            poke_abilities()
        elif selection == 4:
            poke_habitat()
        elif selection == 5:
            poke_type()
        elif selection == 6:
            salir()


def poke_generation():
    # Total de generaciones
    n_totalgeneration = requests.get(pokeapi_url).json()["results"]
    print(f"\n Para iniciar debemos mencionar que en el mundo pokemon ")
    print(f"existen un total de {len(n_totalgeneration)} generaciones")
    print(f"que son los siguientes: \n")
    for i in range(1,len(n_totalgeneration)+1):
        name_generation = requests.get(pokeapi_url+str(i)).json()["main_region"]["name"]
        print(f"{i}: {name_generation}")

    # Escogemos la generación de pokemons
    generation = input("\n Ingrese la generación de pokemons que quiere consultar: ")
    
    print(f"\n La lista de pokemons es el siguiente: \n")
    time.sleep(3)
    list_pokemons = requests.get(pokeapi_url + generation).json()["pokemon_species"]
    for pokemon in list_pokemons:
        pokemons = [pokemon['name'] for pokemon in list_pokemons]
    print(pokemons)
    print("\n")
    time.sleep(3)

def poke_form():
    print("Opción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y se listan todos los pokemons respectivos.")

def poke_abilities():
    print("Opción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.")

def poke_habitat():
    print("Opción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.")

def poke_type():
    print("Opción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar para interactuar.")

def salir():
    print("Gracias por usar nuestra aplicación")

menu()