import requests
import json
from pprint import pprint
from logger2 import logger

path = "app.log"

@logger(path)
def get_the_smartest_superhero(superheroes):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    the_smartest_superhero = ''
    max_intelligence = 0
    dict_int_heroes = {}
    if response.status_code == 200:
        superheroeslist = response.json()
        for hero in superheroeslist:
            if hero["id"] in superheroes:
                intelligence = hero["powerstats"]["intelligence"]
                if hero["name"] not in dict_int_heroes:
                    dict_int_heroes[hero["name"]] = intelligence

                if intelligence > max_intelligence:
                    max_intelligence = intelligence
                    the_smartest_superhero = hero["name"]
    else:
        print("API error")
    print(dict_int_heroes)
    return the_smartest_superhero


if __name__ == "__main__":
    superheroes = [1, 2, 3, 4, 5]
    print(get_the_smartest_superhero(superheroes))