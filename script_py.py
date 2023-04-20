import sqlite3

# Connect to the database
conn = sqlite3.connect('nouvelledb.db')

# Create a cursor
cursor = conn.cursor()

while True:
    print("|||Menu principal : ")
    print("|||1. Afficher les tournois par jeu")
    print("|||2. liste des tournois par lieu")
    print("|||3. Afficher le salaire moyen des joueurs par jeu")
    print("|||2. Quitter")
    menu_choice = int(input("|||Choisissez une option : "))
    if menu_choice == 1:
        # Get the list of games in the database

        cursor.execute("SELECT name from game;")
        games = cursor.fetchall()

        # Print the list of games

        print("Liste des jeux disponibles : ")
        for i, game in enumerate(games):
            print(f"{i+1}. {game[0]}")

        # Ask the user to choose a game

        game_choice = int(input("Choisissez un jeu : "))
        chosen_game = games[game_choice-1][0]

        # Execute a query to get all tournaments for the chosen game

        cursor.execute(f'''SELECT  tournament.date, Place.name, Place.adress,        Place.city
        FROM Tournament 
        INNER JOIN game 
        ON Tournament.IdGame = Game.IdGame
        INNER JOIN Place ON Tournament.IdPlace = Place.IdPlace
        WHERE Game.name = "{chosen_game}";''')

        # Get the column names
        columns = [desc[0] for desc in cursor.description]

        # Get the data from the query
        data = cursor.fetchall()

        # Print the data
        print(f"Tournois pour le jeu {chosen_game} :")
        print(" | ".join(columns))
        print("-" * (3 * len(columns) - 1))
        for row in data:
            print(" | ".join([str(item) for item in row]))
       
    if menu_choice == 2:
        #get the list of the place in the database

        cursor.execute("SELECT name from place;")
        places = cursor.fetchall()

        #print the list of places

        print("Liste des lieux disponibles : ")
        for i, place in enumerate(places):
            print(f"{i+1}. {place[0]}")
        
        #Ask the user to choose a place

        place_choice = int(input("Choisissez un lieu : "))
        chosen_place = places[place_choice-1][0]
        #Execute a query to get all tournaments for the chosen place

        cursor.execute(f'''SELECT Game.name,  tournament.date, Place.name, Place.adress,        Place.city
        FROM Tournament
        INNER JOIN place
        ON Tournament.IdPlace = Place.IdPlace
        INNER JOIN Game ON Tournament.IdGame = Game.IdGame
        WHERE Place.name = "{chosen_place}";''')

        #Get the column names

        columns = [desc[0] for desc in cursor.description]
        #Get the data from the query

        data = cursor.fetchall()
        #Print the data

        print(f"Tournois pour le lieu {chosen_place} :")
        print(" | ".join(columns))
        print("-" * (3 * len(columns) - 1))
        for row in data:
            print(" | ".join([str(item) for item in row]))



    if menu_choice == 3:
        #get the list of the game in the database

        cursor.execute("SELECT name from game;")
        games = cursor.fetchall()

        # Print the list of games

        print("Liste des jeux disponibles : ")
        for i, game in enumerate(games):
            print(f"{i+1}. {game[0]}")

        # Ask the user to choose a game

        game_choice = int(input("Choisissez un jeu : "))
        chosen_game = games[game_choice-1][0]

        #get all the wages from database

        cursor.execute(f'''SELECT AVG(Wage) 
        FROM Player
        INNER JOIN Employee_Data ON idEmployee = idEmployeeData
        INNER JOIN Game ON Player.IdGame = Game.IdGame
        WHERE Game.name = "{chosen_game}";''')

        
       #Get the column names

        columns = [desc[0] for desc in cursor.description]
        #Get the data from the query

        data = cursor.fetchall()
        #Print the data

        print(f"Le Salaire moyen des joueurs de {chosen_game} :")
        print(" | ".join(columns))
        print("-" * (3 * len(columns) - 1))
        for row in data:
            print(" | ".join([str(item) for item in row]))

    if menu_choice == 4:
        print("adios!")
        break
        
# Close the connection
conn.close()