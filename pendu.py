# ##JEU DU PENDU

# from donnees import donnees ##importation du module donnees qui contient l'affichage des scores et des joueurs
import random
# import time



# donnees.start_game()


hp = 8
path1 = "./donnees/mots.txt"

lettre_pas_dans_le_mot = []
stop_words = ["#","?","§","!","*","-","+",".","{","^",":","/"] 


with open(path1, "r") as file:
    mots = [mot.lower().strip() for mot in file] # convertir tous les mots du fichier pour enlever les retours à la ligne
    choix_mot_machine = list(random.choice(mots)) ##prise d'un mot dans le fichier + conversion en liste 
    # print(choix_mot_machine)

mot_a_deviner = ['#' for _ in choix_mot_machine] ##création de d'une liste #

print(mot_a_deviner) 


while hp>0:

    demande = input("Quelle lettre : ")

    if demande.isdigit() or demande in stop_words:  ##gestion des erreurs
        print("Ce n'est pas une lettre", end=", ")
        continue 

    elif demande in lettre_pas_dans_le_mot:
        print("Vous avez déjà écrit cette lettre")
        continue

    for i, lettre in enumerate(choix_mot_machine):
        if demande == lettre:
            mot_a_deviner[i] = demande
        
    if demande not in choix_mot_machine:
        hp-=1
        lettre_pas_dans_le_mot.append(demande)
        print(f"Cettre lettre n'est pas dans le mot \n, ces lettres ne sont pas dans le mot {lettre_pas_dans_le_mot}\n il vous reste {hp} vies")

    print(mot_a_deviner)

    if "#" not in mot_a_deviner:
        print(f"Vous avez gagné !! , le mot était {mot_a_deviner}")
        break

print("Vous n'avez plus de vies ! Perdu")
    
