import requests
import json
import time

class Pokemon:
    def __init__(self, pokeapi_url):
        self.pokeapi_url = pokeapi_url

    def menu(self):
        selection = 0
        while selection != 6:
            print("\nBienvenidos a la aplicacion de consultas sobre los pokemons")
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
                self.poke_generation()
            elif selection == 2:
                self.poke_form()
            elif selection == 3:
                self.poke_abilities()
            elif selection == 4:
                self.poke_habitat()
            elif selection == 5:
                self.poke_type()
            elif selection == 6:
                self.salir()

    def poke_generation(self):
        # Total de generaciones
        print(f"\n >> 1.- POKEMOS POR GENERACIÓN <<")
        url_generacion = self.pokeapi_url+'/generation/'
        n_totalgeneration = requests.get(url_generacion).json()["results"]
        print(f"\n Para iniciar debemos mencionar que en el mundo pokemon ")
        print(f"existen un total de {len(n_totalgeneration)} generaciones")
        print(f"que son los siguientes: \n")
        for i in range(1,len(n_totalgeneration)+1):
            name_generation = requests.get(url_generacion+str(i)).json()["main_region"]["name"]
            print(f"{i}: {name_generation}")

        # Escogemos la generación de pokemons
        generation = input("\n Ingrese la generación de pokemons que quiere consultar: ")
        
        print(f"\n La lista de pokemons es el siguiente: \n")
        time.sleep(2)
        list_pokemons = requests.get(url_generacion + generation).json()["pokemon_species"]
        for pokemon in list_pokemons:
            pokemons = [pokemon['name'] for pokemon in list_pokemons]
        print(pokemons)
        print("\n")
        time.sleep(2) 

    def poke_form(self):
        pass

    def poke_abilities(self):
        pass

    def poke_habitat(self):
        pass

    def poke_type(self):
        pass

    def salir(self):
        pass


url = Pokemon("https://pokeapi.co/api/v2")
url.menu()