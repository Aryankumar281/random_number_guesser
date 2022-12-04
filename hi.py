import random
guess_done= 0
count=0
welcome='''
|   |  ____ |     ___  ___   |\   /|  ____
| ^ | |__   |    |    /   \  | \/  | |__
|/ \| |____ |___ |___ \___/  |     | |____]
      _______ 
         |    ____
         |   /    \ 
         |   \____/
 ___               ___   ___                                                 ____
|___|  /\   |\  | |   \ |   | |\  /|       |\  |            __   ___   _    |           __   __   __   __   _
|\    /__\  | \ | |   | |   | | \/ |       | \ | |  | |\/| |__| |__   |_|   |  __ |  | |__| |__  |__  |__| |_|
| \  /    \ |  \| |___/ |___| |    |       |  \| |__| |  | |__| |___  |\    |___| |__| |___ ___| ___| |___ |\  

'''
print(welcome)
print("Hi! What is your name?")
myname = input("Your name: ")
if myname.isalpha():
    print(f"Tell me,{myname} that in which range of numbers, Do you want to guess that number ?")
    lower_bound=int(input("Enter minimum value:"))
    upper_bound=int(input("Enter maximum value:"))
    number = random.randint(lower_bound,upper_bound)
    print(f'Well,{myname},I am thinking of a number between {lower_bound} to {upper_bound}😊.')
    print("\n\tYou have 3 Chances to Guess ")
    while guess_done<3:
        guess =int(input("Enter Your Number:- "))
        guess_done = guess_done+1
        if guess < number:
            print("Have One More Try.Your guess is too low!🙄")
        if guess > number:
            print("Have One More Try.Your guess is too high!🥱")
        if guess==number:
            count=count+1
            break
    if guess==number:
        print(f"\n\tCongratulations✌, {myname}, You guessed my number in {guess_done} guesses!")
    if guess !=number:
        print(f"Nope😁.The number I was thinking is {number}.")
        print("Better luck next time")
else:
    print("Enter a valid input")