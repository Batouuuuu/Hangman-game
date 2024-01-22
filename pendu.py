##JEU DU PENDU

import random
import time

data = {}
player_name = input("Nom : ").title().strip()

if player_name not in data:
    data[player_name] = 0




hp = 8

path = "./donnees/mots.txt"

word_to_guess = []
letter_not_in_word = []
letter_in_word = []

with open(path, "r") as file:
    mots = [mot.lower().strip() for mot in file] # convertir tous les mots du fichier pour enlever les retours à la ligne
    machine_choice = random.choice(mots)
    # print(machine_choice)

    for letter in machine_choice:    ##parcours des lettres du mot et ajout dans la liste 
        word_to_guess.append(letter)
   
    print(word_to_guess)

for _ in range(len(word_to_guess)):
    letter_in_word.append("*")
print(letter_in_word)




while hp >= 1:
    
    ask = input("lettre: ").lower().strip()
     

    if ask in word_to_guess:    
        print("Cette lettre est dans le mot")
        print(letter_in_word)
    else:
        hp -= 1
        letter_not_in_word.append(ask)
        print("Il n'y pas cette lettre dans le mot, il vous reste ", hp, "vies") 
        time.sleep(1)
        print("Ces lettres ne sont pas dans le mot : ",letter_not_in_word) 

    if hp == 0:
        print("perdu")

    





