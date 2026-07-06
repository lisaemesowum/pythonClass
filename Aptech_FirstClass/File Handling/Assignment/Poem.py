import random

file_path = "Players_Name.txt"

while True:
    print("\n|----------------------Poem Game group----------------------------|\n")
    print("| 1:  Start Poem Game \n")
    game = input("| Enter Game - ")
    if game == "1":
        try:
            number_of_players = int(input("\n| Enter numbers of players -  "))
        except ValueError:
            print("Enter a number")
        players_names = input("\n| Enter players names - ")
        with open("Aptech_FirstClass/File Handling/Assignment/Players_Name.txt", "w") as file:
            file.write("---------------------------------------------------------------------\n\n")
            file.write(f"Number of Players - {number_of_players}\n")
            file.write(f"Players Names - {players_names} \n")
        # read the names from the file
        with open("Aptech_FirstClass/File Handling/Assignment/Players_Name.txt", "r") as file:
            players = players_names.split()
        # randomly shuffle the names 
        random.shuffle(players)
        print(players)
        # after shuffling add it back
        with open("Aptech_FirstClass/File Handling/Assignment/shuffle_players.txt", "w") as file:
            for player in players:
                file.write(f"{player}\n")
        print("players added \n\n")
        # for the stuffled player
        while True:
            print("\n Poem game starting ----- \n")
            print("1: Start \n")
            start = input("\nOption to start: ")
            if start == "1":
                for player in players:
                    print(f"{player}, your turn \n")
                    line = input("write Your Poem: ") 
                    with open("Aptech_FirstClass/File Handling/Assignment/poem.txt", "a") as file:
                        file.write(line + "\n")
                print("Game over")
                break
                    
 
        
        
        