import random
'''
#first version where you are guessing computer`s number
def answer(x):
    random_number = random.randint(1, x)
    answer = 0

    while answer != random_number:
        answer = int(input(f"guess the number between 1 and {x}: "))
        if answer < random_number:
            print("too low")
        elif answer > random_number:
            print("too high")
    print("yay, you have guessed the number")
answer(10)
'''

#secodnd version where the computer is guessing

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            answer = random.randint(low, high)
        else:
            answer = low
        feedback = input(f"is {answer} too high (H), too low (L) or correct (C) ?").lower()
        if feedback == "h":
            high == guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f" computer guessed the number {answer} correctly")


computer_guess(10)