import csv
path = "./test.csv"
meilleur_score = 0

with open(path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|') 

    for row in csv_reader: 
        score = int(row[0])
        if score > meilleur_score:
            meilleur_score = score
        

    print(meilleur_score)
         

