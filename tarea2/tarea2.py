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
      print(f"\n >> 1.- POKEMOS POR FORMA <<")
      shape_url = self.pokeapi_url+'/pokemon-shape/'
      result = requests.get(shape_url).json()["results"]
      print(f"\n Debemos mencionar que en el mundo pokemon existen un total de {len(result)} formas de pokemon que son los siguientes: \n")
      for i in range(0, len(result)):
        print(f"{i+1}: {result[i]['name']}")
      shape = input("\n Ingrese el numero correspondiente a la forma de pokemons que quiere consultar: ")
      selected_shape = requests.get(shape_url+shape).json()['pokemon_species']
      
      print("Los pokemons que poseen esta forma son los siguientes: ")
      for i in range(1,len(selected_shape)):
        print(f"{i}: {selected_shape[i]['name']}")

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
                print(lista)
            else:
                image = str(pokemon['pokemon']['url'])
                poke_image = requests.get(image).json()['sprites']['front_default']
                lista.append(f"- {pokemon['pokemon']['name']} : {poke_image}")
                print(lista[-1])

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
            image = pokemon['url']
            poke_image = requests.get(str(image)).json()['varieties']
            for row in poke_image:
                poke = row['pokemon']['url']
            image_poke = requests.get(str(poke)).json()['sprites']['front_default']
            lista.append(f"- {pokemon['name']}: {image_poke}")
            print(lista[-1])

    def poke_type(self):
      print(f"\n >> 1.- POKEMOS POR TIPO <<")
      type_url = self.pokeapi_url+'/type/'
      result = requests.get(type_url).json()["results"]
      print(f"\nDebemos mencionar que en el mundo pokemon existen un total de {len(result)-1} tipos de pokemon que son los siguientes: \n")

      for i in range(1,len(result)):
        print(f"{i}: {result[i]['name']}")

      type = input("\n Ingrese el numero correspondiente al tipo de pokemons que quiere consultar: ")
      selected_type = requests.get(type_url+type).json()['pokemon']
      
      print("Los pokemons que poseen este tipo son los siguientes: ")
      for i in range(1,len(selected_type)):
        print(f"{i}: {selected_type[i]['pokemon']['name']}")

    def salir(self):
        pass


url = Pokemon("https://pokeapi.co/api/v2")
url.menu()