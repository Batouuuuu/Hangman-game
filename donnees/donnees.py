import csv

def players(path):

    player_name = input("User : ").title().strip()
    score = 0

    existing_players = [] 

    with open(path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|') 

        for row in csv_reader:
            best_player = row["Score"]
            print("Le meilleur joueur actuellement est : avec un score de ")
            if player_name == row["User"]:
                existing_players.append(row["User"]) # ajout du nom du joueur à la liste des joueurs existants
                print(f"Bon retour parmi nous {row['User']} ton score était de {row['Score']} points")
            
        if player_name not in existing_players:
            with open(path, 'a', newline='') as csvfile:
                print(f"Bienvenue parmi-nous nouveau joueur : {player_name}")
                new_player = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                new_player.writerow((player_name,score)) #utilisation d'un tuple car writerow ne prend qu'un argument
    
    return
        
players(".//data_players.csv")


