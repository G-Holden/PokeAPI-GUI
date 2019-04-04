from tkinter import *
from pokeapi import *

smallFont = ["Helvetica" , 14]
mediumFont = ["Helvetica" , 18]
bigFont = ["Helvetica" , 30]

pokedexNo = 0

def showPokemonData():
    global pokedexNo
    #get the number typed into the entry box
    pokemonNumber = int(txtPokemonNo.get())
    pokedexNo = pokemonNumber
    #use the function in the 'pokeapi.py' file to get pokemon data
    pokemonDictionary = getPokemonData(pokemonNumber)
    #get the data from the dictionary and add it to the labels
    configurePokemonData(pokemonDictionary)

def getNextPokemon(): 
    global pokedexNo
    pokemonNumber = updateDexNo(1)
    txtPokemonNo.delete(0, END)
    #use the function in the 'pokeapi.py' file to get pokemon data
    pokemonDictionary = getPokemonData(pokemonNumber)
    #get the data from the dictionary and add it to the labels
    configurePokemonData(pokemonDictionary)

def configurePokemonData(pokemonDictionary):
    lblNameValue.configure(text = pokemonDictionary["name"])
    lblHPValue.configure(text = pokemonDictionary["HP"])
    lblAttackValue.configure(text = pokemonDictionary["attack"])
    lblDefenceValue.configure(text = pokemonDictionary["defence"])
    lblSpeedValue.configure(text = pokemonDictionary["speed"])
    
def updateDexNo(add = 0):
    global pokedexNo
    pokedexNo += add
    return pokedexNo
    

#create a new GUI window
window = Tk()
window.config(bg="#e0e0ff")
window.title("Pokedex")
window.geometry('220x500')

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

btnNext = Button(window,text="Next > ", command=getNextPokemon)
btnNext.pack()

btnPrev = Button(window,text="< Prev ", command=getNextPokemon)
btnNext.pack()

#labels for the pokemon data
lblNameText = Label(window,text="Name:")
lblNameText.pack()
lblNameText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblNameValue = Label(window,text="???")
lblNameValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblNameValue.pack()

lblHPText = Label(window,text="HP:") # stat no: /1 (5)
lblHPText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblHPText.pack()
lblHPValue = Label(window,text="0")
lblHPValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblHPValue.pack()

lblAttackText = Label(window,text="Attack:") #stat number: /2 (index 4)
lblAttackText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblAttackText.pack()
lblAttackValue = Label(window,text="0")
lblAttackValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblAttackValue.pack()

lblDefenceText = Label(window,text="Defence:") #stat number: /3 (index 3)
lblDefenceText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblDefenceText.pack()
lblDefenceValue = Label(window,text="0")
lblDefenceValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblDefenceValue.pack()

lblSpeedText = Label(window,text="Speed:") #stat number: /6 (index 0)
lblSpeedText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblSpeedText.pack()
lblSpeedValue = Label(window,text="0")
lblSpeedValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblSpeedValue.pack()

window.mainloop()
