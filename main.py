import random
import pyttsx3

motor=pyttsx3.init('sapi5')
voices=motor.getProperty('voices')

motor.setProperty('voice',voices[0].id)




def speak(audio):
    motor.say(audio)
    motor.runAndWait()

if __name__ == "__main__":
    speak("Welcome to Dragon, Water and Fire game")



print("DRAGON WATER FIRE")
print(" ---------------")
Shape = ["D", "W", "F"]
userScore = 0
computerScore = 0
i = 1
while i <= 5:
    computerShape = str(random.choice(Shape))
    userShape = input("Enter Dragon, Water Fire (key: D,F,W): ").upper()
    if userShape == computerShape:
        print("It's a Tie ")
    elif computerShape == "W" and userShape == "D":
        print(("Computer Enter", computerShape))
        print(" Dragon Drink Water")
        userScore += 1
    elif computerShape == "D" and userShape == "W":
        print(("Computer Enter", computerShape))
        print(" Dragon Drink Water")
        computerScore += 1
    elif computerShape == "F" and userShape == "W":
        print(("Computer Enter", computerShape))
        print(" Fire turned off by water ")
        userScore += 1
    elif computerShape == "W" and userShape == "F":
        print(("Computer Enter", computerShape))
        print("Fire turned off by water")
        computerScore += 1
    elif computerShape == "D" and userShape == "F":
        print(("Computer Enter", computerShape))
        print("Fire destroyed Dragon")
        userScore += 1
    elif computerShape == "F" and userShape == "D":
        print(("Computer Enter", computerShape))
        print("Fire destroyed Dragon")
        computerScore += 1
    else:
        print("Invalid input:(")
    print("\n\t******ScoreBoard******")
    print(f"\t You: {userScore} | Computer: {computerScore}")
    p=5-i
    print(f"More {p} Games left")
    
    i += 1
print("\n\n*** Game Ended ***")
if userScore < computerScore:
      speak(
        f"You lost the game \n computer won the "
        f"game with {computerScore} score"
    )
        
elif userScore == computerScore:
    speak("It's Tie Play Again ")
         


       
else:
     speak(f"Congrats You Won the Game with {userScore} score ")

       

    
