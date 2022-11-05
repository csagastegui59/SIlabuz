
import requests
import json

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
        pass 

    def poke_form(self):
        pass

    def poke_abilities(self):
        print("\nOpción 3: Listar pokemons por habilidad.")
        url_ability = str(self.pokeapi_url +'/ability/')
        n_totalability = requests.get(url_ability).json()['count']
        print(f"\nDebemos mencionar que en el mundo pokemon existen un total de {int(n_totalability)} habilidades")
        print(f"Las cuales son las siguientes: \n")
        count = 10000
        for i in range(1,int(n_totalability)+1):
            if i > 267:
                count += 1
                name_ability = requests.get(url_ability+str(count)).json()["name"]
                print(f"{count}: {name_ability}")
            else: 
                name_ability = requests.get(url_ability+str(i)).json()["name"]
                print(f"{i}: {name_ability}")
        
        ability = int(input("\nIngrese el número de la habilidad que quiera consultar: "))
        list_pokemons = requests.get(url_ability + str(ability)).json()['pokemon']
        print(f"\nPokemon con esta habilidad: {len(list_pokemons)}\n")
        lista = []
        for pokemon in list_pokemons:
            if int(ability) > 267:
                lista.append(list_pokemons)
            else:
                lista.append(pokemon['pokemon']['name'])
        print(lista)

    def poke_habitat(self):
        print("\nOpción 4: Listar pokemons por habitat.")
        url_habitat = str(self.pokeapi_url +'/pokemon-habitat/')
        n_totalhabitat = requests.get(url_habitat).json()['results']
        print(f"\nEn el mundo pokemon existen un total de {len(n_totalhabitat)} habitats")
        print(f"Las cuales son las siguientes: \n")
        for i in range(1,len(n_totalhabitat)+1):
            name_habitat = requests.get(url_habitat+str(i)).json()["name"]
            print(f"{i}: {name_habitat}")
        habitat = int(input("\nIngrese el número del hábitat que quiera consultar: "))
        list_pokemons = requests.get(url_habitat + str(habitat)).json()['pokemon_species']
        print(f"\nLas especies de Pokemón que viven en esta hábitat son:\n")
        lista = []
        for pokemon in list_pokemons:
            lista.append(pokemon['name'])
        print(lista)

    def poke_type(self):
        pass

    def salir(self):
        pass


url = Pokemon("https://pokeapi.co/api/v2")
url.menu()