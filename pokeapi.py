import io
import json
import urllib.request
from urllib.request import urlopen

#function to get the data for a pokemon
def getPokemonData(num):
    url = "http://pokeapi.co/api/v1/pokemon/"+str(num)
    request = urllib.request.Request(url)
    request.add_header('User-Agent', "something")
    data = urllib.request.urlopen(request).read()
    pokemonDict = json.loads(data.decode("UTF-8"))
    createStatsData(pokemonDict)
    return pokemonDict

#creates dictionary entries equivalent to the ones in code club instructions
def createStatsData(pokemonDict):
    pokemonDict["HP"] = pokemonDict["stats"][5]["base_stat"]
    pokemonDict["attack"] = pokemonDict["stats"][4]["base_stat"]
    pokemonDict["defence"] = pokemonDict["stats"][3]["base_stat"]
    pokemonDict["speed"] = pokemonDict["stats"][0]["base_stat"]



   
