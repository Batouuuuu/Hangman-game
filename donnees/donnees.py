import csv


###pour des raisons de simplicité le fichier csv contient 2 colonnes la première USER et l'autre Score, c'est intitulés ne figurent pas car problème pour extraire les données sinon

def print_score(path, player_name):
    """"Affichage des scores et appel de la fonction get_best_player"""

    score = 0
    existing_players = []

    with open(path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|') 

        for row in csv_reader:
            
            if player_name == row[0]:
                existing_players.append(row[0]) # ajout du nom du joueur à la liste des joueurs existants
                print(f"Bon retour parmi nous {row[0]} ton score était de {row[1]} points")
                get_best_player(row, score)
            

                
            
            if player_name not in existing_players:
                create_new_player(path, player_name, score)
    
    
 

def get_best_player(row, score):
    """"Obtenir le joueur qui a le meilleur score et convertir le colonne des scores en int"""

    convert = int(row[1]) # conversion des scores en integer           
    if convert > score:
        score = convert
        get_best_user = row[0]
        print(f"Le meilleur joueur actuellement est : {get_best_user} avec un score de {score} ")
    return score


def create_new_player(path, player_name, score):
    """"Création d'un nouveau joueur"""

    with open(path, 'a', newline='') as csvfile:
        print(f"Bienvenue parmi-nous nouveau joueur : {player_name}")
        new_player = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        new_player.writerow((player_name,score)) #utilisation d'un tuple car writerow ne prend qu'un argument


def start_game():
    player_name = input("User : ").title().strip()
    print_score("./data_players.csv", player_name) 
start_game()