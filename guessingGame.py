import random

print("""

1Number Guessing Game


""")
print("Instructions: Guess a number between 1 and 9, including 1 and 9")
num= random.randint(1, 9)
chances=0
while chances<=5:
    guess=int(input("Enter your guess "))

    if (guess<num):
        print("Your guess was too low. Guess a number higher than", guess)
        chances+=1
    elif(guess>num):
        print("Your guess was too high. Guess a number lower than", guess)
        chances+=1

    else:
        print("Congrats! You got it!")
        break
if not chances<=5:
    print("Sorry, you lost. The number is", num)