from tkinter import *
from pokeapi import *

def showPokemonData():
    #get the number typed into the entry box
    pokemonNumber = int(txtPokemonNo.get())
    #use the function in the 'pokeapi.py' file to get pokemon data
    pokemonDictionary = getPokemonData(pokemonNumber)
    #get the data from the dictionary and add it to the labels
    configurePokemonData(pokemonDictionary)

def getAdjacentPokemon(val):
    #get the current Pokemon's Dex number
    pokemonNumber = int(lblDexNoValue.cget("text")) + val
    txtPokemonNo.delete(0, END)
    #use the function in the 'pokeapi.py' file to get pokemon data
    pokemonDictionary = getPokemonData(pokemonNumber)
    #get the data from the dictionary and add it to the labels
    configurePokemonData(pokemonDictionary)

def configurePokemonData(pokemonDictionary):
    lblNameValue.configure(text = pokemonDictionary["name"][0].upper()+ pokemonDictionary["name"][1:])
    lblDexNoValue.configure(text = pokemonDictionary["id"])
    lblHPValue.configure(text = pokemonDictionary["HP"])
    lblAttackValue.configure(text = pokemonDictionary["attack"])
    lblDefenceValue.configure(text = pokemonDictionary["defence"])
    lblSpeedValue.configure(text = pokemonDictionary["speed"])

#font formatting for labels
smallFont = ["Helvetica" , 14]
mediumFont = ["Helvetica" , 18]
bigFont = ["Helvetica" , 30]

#create a new GUI window
window = Tk()
window.config(bg="#e0e0ff")
window.title("Pokedex")
window.geometry('220x550')

#a label containing the instructions
lblInstructions = Label(window,text="Enter a number between 1 and 807:")
lblInstructions.config(bg="#e0e0ff", fg="#111111")
lblInstructions.pack()

#an 'entry' textbox for typing in the pokemon number
txtPokemonNo = Entry(window)
txtPokemonNo.pack()

#a button that will get the info for a pokemon
btnGetInfo = Button(window,text="Get Data!", command=showPokemonData)
btnGetInfo.pack()

#buttons controlling Next & Prev functionality
btnNext = Button(window,text="Next > ", command= lambda: getAdjacentPokemon(1))
btnNext.pack()

btnPrev = Button(window,text="< Prev ", command= lambda: getAdjacentPokemon(-1))
btnPrev.pack()

#labels for the pokemon data
lblNameText = Label(window,text="Name:")
lblNameText.pack()
lblNameText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblNameValue = Label(window,text="???")
lblNameValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblNameValue.pack()

lblDexNoText = Label(window,text="Pokédex No:")
lblDexNoText.pack()
lblDexNoText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblDexNoValue = Label(window,text="???")
lblDexNoValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblDexNoValue.pack()

lblHPText = Label(window,text="HP:")
lblHPText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblHPText.pack()
lblHPValue = Label(window,text="0")
lblHPValue.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblHPValue.pack()

lblAttackText = Label(window,text="Attack:")
lblAttackText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblAttackText.pack()
lblAttackValue = Label(window,text="0")
lblAttackValue.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblAttackValue.pack()

lblDefenceText = Label(window,text="Defence:")
lblDefenceText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblDefenceText.pack()
lblDefenceValue = Label(window,text="0")
lblDefenceValue.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblDefenceValue.pack()

lblSpeedText = Label(window,text="Speed:")
lblSpeedText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblSpeedText.pack()
lblSpeedValue = Label(window,text="0")
lblSpeedValue.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblSpeedValue.pack()

window.mainloop()
