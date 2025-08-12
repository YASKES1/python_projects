low = 1
high = 1000
print(f"Please think about the number between {low} and {high}")
input("Press ENTER to start")

guesses = 1

while low != high:
    print(f"\tGuessing in the range from {low} to {high} ")
    guess = low + (high - low) // 2
    high_low = input(f"My guess is {guess}."
                     f" Should i guess higher or lower? "
                     f"Enter h or low or c if correct  "
                     .casefold())

    if high_low == "h":
        # guess higher the low end of the range
        # becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower the high end of the range
        # becomes one less than the guess
        high = guess - 1
    elif high_low == "c":
        print(f"I got it in {guesses} guesses!")
        break
    else:
        print("Please enter h,l or c")
    guesses += 1
else:
    print(f"You thought of the number {low}")
    print(f"i've got it in {guesses} guesses")




