import random

print("A colors guessing game")
colors = ["pink","red","blue","green","yellow","black","white"]
user_playing = input("do you want to play ? ")

while user_playing.lower() == "yes":
    random_color = colors[random.randint(0,6)]
    user_guess = input("Guess the color i'm thinking about : ")
    while(user_guess.lower() != random_color):
        user_guess = input("Wrong ! try again : ")
    print("Correct ! I was thinking of",random_color)
    user_playing = input("Another round ? : ")
print("Thank you for playing the game with me !")
