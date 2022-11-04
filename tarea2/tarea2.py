
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
        pass

    def poke_habitat(self):
        pass

    def poke_type(self):
        pass

    def salir(self):
        pass


url = Pokemon("https://pokeapi.co/api/v2")
url.menu()