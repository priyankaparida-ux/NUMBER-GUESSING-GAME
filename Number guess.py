# NUMBER GUESSING GAME
import random
num1 = random.randint(1,100)
while True:
    num2 = int(input("Guess the number between 1 to 100: "))
    if (num2 == num1):
        print("Congratulations!! You guessed the correct number")
        break
    elif(num2 < num1):
        print("Too low!! Try one more time")
    else:
        print("Too high!! Try one more time")
        
