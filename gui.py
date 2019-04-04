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

#buttons controlling Next & Prev functionality
buttonFrame = LabelFrame(window)
buttonFrame.config(bg="#e0e0ff", fg="#111111")
buttonFrame.pack(pady=10)

btnPrev = Button(buttonFrame,text="< Prev ", command= lambda: getAdjacentPokemon(-1))
btnPrev.pack(ipadx=5,side=LEFT)

#a button that will get the info for a pokemon
btnGetInfo = Button(buttonFrame,text="Get Data!", command=showPokemonData)
btnGetInfo.pack(padx=5,side=LEFT)

btnNext = Button(buttonFrame,text="Next > ", command= lambda: getAdjacentPokemon(1))
btnNext.pack(ipadx=5,side=LEFT)


#creating labelFrame
labelFrame = LabelFrame(window, text="Pokémon Information")
labelFrame.config(bg="#e0e0ff", fg="#111111", font=smallFont)
labelFrame.pack(fill="both", expand="yes")

#labels for the pokemon data
lblNameText = Label(labelFrame,text="Name:")
lblNameText.pack()
lblNameText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblNameValue = Label(labelFrame,text="???")
lblNameValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblNameValue.pack()

lblDexNoText = Label(labelFrame,text="Pokédex No:")
lblDexNoText.pack()
lblDexNoText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblDexNoValue = Label(labelFrame,text="???")
lblDexNoValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblDexNoValue.pack()

lblHPText = Label(labelFrame,text="HP:")
lblHPText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblHPText.pack()
lblHPValue = Label(labelFrame,text="0")
lblHPValue.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblHPValue.pack()

lblAttackText = Label(labelFrame,text="Attack:")
lblAttackText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblAttackText.pack()
lblAttackValue = Label(labelFrame,text="0")
lblAttackValue.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblAttackValue.pack()

lblDefenceText = Label(labelFrame,text="Defence:")
lblDefenceText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblDefenceText.pack()
lblDefenceValue = Label(labelFrame,text="0")
lblDefenceValue.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblDefenceValue.pack()

lblSpeedText = Label(labelFrame,text="Speed:")
lblSpeedText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblSpeedText.pack()
lblSpeedValue = Label(labelFrame,text="0")
lblSpeedValue.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblSpeedValue.pack()

window.mainloop()
