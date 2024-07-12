import random 

computer_guess = random.randint(1,100)
user_input = int(input('Enter a number:'))
if computer_guess == user_input:
    print ("Win")
else:
    print(f"The computer guess {computer_guess}. Your own guess is {user_input} you lost ")