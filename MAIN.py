import random

# Generate a random number from 1 to 3

computer = random.randint(1, 3)


# 1 -> Rock
# 2 -> paper
# 3 -> scissor



print("----------------------------------")
print("Welcome to Rock, paper, scissor Game")
print("Choose from following choices")
print(
        """1 -> Rock
2 -> paper
3 -> scissor"""
    )

Player = int(input("Enter your choice: "))

if Player > 3 or Player < 1:
    print("Invalid choice, Please choose form given choices")

elif computer == 1 and Player == 1:
    print("DRAW!")

elif computer == 1 and Player == 2:
    print("You Win, Congratulaitons")

elif computer == 1 and Player == 3:
    print("You Loose")

elif computer == 2 and Player == 1:
    print("You Loose")

elif computer == 2 and Player == 2:
    print("DRAW!")

elif computer == 2 and Player == 3:
    print("You Win, Congratulaitons")

elif computer == 3 and Player == 1:
    print("You Win, Congratulaitons")

elif computer == 3 and Player == 2:
    print("You Loose")

elif computer == 3 and Player == 3:
    print("DRAW!")
