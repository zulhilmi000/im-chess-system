TEXT_FILE="ratings.txt"
START_RATING= 1000
K = 40

#CALCULATION FOR RATING
def calculation_main(rank_player1, rank_player2, score1):
    total=rank_player1 + K * (score1 - calculation_sec(rank_player2,rank_player1))
    return total

def calculation_sec (rank_player2,rank_player1):
    total=1 / (1 + 10 ** ((rank_player2 - rank_player1) / 400))
    return total

#SEARCH RATING
def search_rating():
        #STORE IN DICTIONARY
        ratings = {}
        try:
            with open(TEXT_FILE, "r") as file:
                lines = file.readlines()[1:] 
                for line in lines:
                    parts = line.strip().split()
                    #CHOOSE THE UPPER ONE (WITHOUR HEADER)
                    if len(parts) >= 2:
                        name = parts[0]
                        rating = float(parts[1])
                        #STORE IN DICTIONARY
                        ratings[name] = rating
        #FILE NOT  FOUND DO NOTHING AND KEEP MOVE ON
        except FileNotFoundError:
            pass
        return ratings

#SAVE/UPDATE NEW RATING AFTER MATCH 
def save_rating(ratings):
    with open(TEXT_FILE, "w") as file:
        #WRITE HEADER
        file.write(f"{'PLAYER':<15}RATING\n")
        for name, rating in ratings.items():
            #INSERT NAME AND RATING WITH GOOD INTERFACE 
            file.write(f"{name.upper():<15}{round(rating, 2):.2f}\n")

#INTERFACE OF PROGRAM

def FLOW_SYSTEM():
    #MAKE VARIABLE FOR DICTONARY 
    
    ratings = search_rating()

    #PLAYER NAME

    name1 = input("Enter Player 1 name: ").strip()
    name2 = input("Enter Player 2 name: ").strip()

    #GET THEIR RATING IF EXIST , IF NOT IT WILL BE DEFAULT

    rank_player1 = ratings.get(name1.upper(), START_RATING)
    rank_player2 = ratings.get(name2.upper(), START_RATING)

    #TELL USER ABOUT CURRENT RATING BEFORE PROCCED

    print(f"\nCurrent Ratings:\n{name1.upper()}: {rank_player1}\n{name2.upper()}: {rank_player2}")

    #ENTER THE RESULT (W/L/D) FROM PLAYER 1 PERSPECTIVE

    print("\nEnter result from Player 1's perspective (1 = win, 0.5 = draw, 0 = loss):")
    score1 = float(input(f"{name1.upper()} vs {name2.upper()}: "))

    #THIS IS FOR PLAYER 2 ,IF PLAYER 1 GOT "1" THEN PLAYER 2 WILL BE "0" MEAN HE LOST 

    score2 = 1 - score1

    #ASK FOR CONFIRMATION AGAIN BEFORE FINAL TOUCH

    confirm = input(
        f"Confirm: {name1.upper()} scored {score1} vs {name2.upper()} — "
       
        f"Sure {name1.upper()} {'WON' if score1 == 1 else 'DREW' if score1 == 0.5 else 'LOST'}? (y/n): "
    ).strip().lower()

    #IF USER SAY NO THEN THE PROGRAM WILL BE STOP AND NO CHANGES WILL BE MADE

    if confirm != 'y':
        print("Cancelled. No changes made.")
        return
    
    #CALCULATION FOR NEW RATING

    new_rating1 = calculation_main(rank_player1, rank_player2, score1)
    new_rating2 = calculation_main(rank_player2, rank_player1, score2)

    #CHANGE THE RATING WHEN CALCULATION DONE

    ratings[name1.upper()] = new_rating1
    ratings[name2.upper()] = new_rating2

    #SAVE THE NEW RATING

    save_rating(ratings)

    #TELL USER ABOUT CHANGES

    print(f"\nUpdated Ratings (K={K}):")
    print(f"{name1.upper()}: {round(new_rating1, 2)}")
    print(f"{name2.upper()}: {round(new_rating2, 2)}")


FLOW_SYSTEM()




