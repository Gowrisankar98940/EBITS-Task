user1 = input("What's your name:")
user2 = input("And your name:")
<<<<<<< HEAD
user1_answer = input("%s, do yo want to choose rock, paper or scissors:" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors:" % user2)
=======
user1_answer = input("%s, do yo want to choose rock, paper or scissors:", user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors:", user2)
>>>>>>> cb7805323852e604b1e0262c82acc87cfb7cf983

def compare(u1, u2):
    if u1 == u2:
        return("match draw!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input!, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))
