from time import sleep
import pokebase as pb

#Created a slow print function to make interfacing more fun

def printS(txt):
        for x in txt:
                print (x, end='', flush=True)
                sleep(0.05)
        print()
#print all types
printS("Here is a list of all pokemon types for reference: ")
typelist = pb.APIResourceList('type')
for type in typelist:
        print(type['name'])

#print all names of pokemon of type named here
printS("Please enter a type of pokemon: ")
var = input()
printS("You entered: " + var +". Here is a list of pokemon of that type.")
types = pb.type_(var).pokemon
for poke in types:
        print(poke.pokemon.name)

# Print all moves of the type named here.
printS('Enter a type to see all of the moves associated with it: ')
TYPE = input()
type_moves = pb.type_(TYPE).moves
for move in type_moves:
    print(move.name)

# Get info specific to a certain pokemon
printS('Please enter the name of your favorite pokemon: ')
var = input()
poke = pb.pokemon(var)
w = str(poke.weight)
printS(var + ' weighs a whopping ' + w + ' lbs!!!')
printS(var + ' is in the following games: ')
game_ind = poke.game_indices
for game in game_ind:
        print(game.version.name)

