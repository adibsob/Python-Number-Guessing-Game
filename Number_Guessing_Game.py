import random

# Type 1 - The computer will generate a random number, then you will try to guess it


def guess_random_number(lives, start, stop):
    random_number = random.randrange(start, stop)
    already_guessed = []
    tries = 0
    print("\nI have a number in mind between", start,
          "and", stop, "can you guess what it is?")
    while lives != 0:
        print("You have", lives, "tries left.")
        user_guess = int(input("\nGuess a number: "))
        if user_guess not in already_guessed:
            if user_guess in range(start, stop):
                if user_guess == random_number:
                    print("You guessed correctly")
                    break
                elif user_guess > random_number:
                    print("Your guess is higher than my number")
                    already_guessed.append(user_guess)
                    print("Numbers you already guessed are: ", already_guessed)
                    lives -= 1
                    tries += 1
                elif user_guess < random_number:
                    print("Your guess is smaller than my number")
                    already_guessed.append(user_guess)
                    print("Numbers you already guessed are: ", already_guessed)
                    lives -= 1
                    tries += 1
            else:
                print("Invalid entry, please guess an integer between",
                      start, "and", stop)
        else:
            print("You already guessed that number try a new one")
            continue
    else:
        print("Sorry your ran out of lives and could not guess.")


# guess_random_number(5, 0, 10)

# Type 2 - The computer will generate a random number, then the computer will try to guess it using linear search


def guess_random_num_linear(tries, start, stop):
    random_number = random.randrange(start, stop)
    print("The number for the program to guess is: ", random_number)
    for x in range(start, stop + 1):
        tries -= 1
        print("The program is guessing...", x)
        print("number of tries left: ", tries)
        if x == random_number:
            print("The porogram has guessed the correct number!")
            break
        elif tries == 0:
            print("The program has failed to guess the correct number.")
            break


# guess_random_num_linear(5, 0, 10)

# Type 3 - The computer will generate a random number, then the computer will try to guess it using binary search
def guess_random_num_binary(tries, start, stop):
    random_number = random.randrange(start, stop)
    print("The number for the program to guess is: ", random_number)
    lower_bound = start
    upper_bound = stop + 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        if pivot == random_number:
            print("Found it!", pivot)
            return
        elif pivot > random_number:
            upper_bound = pivot - 1
            print("Guessing higher!")
            tries -= 1
        elif pivot < random_number:
            lower_bound = pivot + 1
            tries -= 1
            print("Guessing lower!")

        if tries == 0:
            print("Program failed to find the number")
            return


# guess_random_num_binary(5, 0, 100)


def ask_user(tries, start, stop):
    print("1) Linear search")
    print("2) Binary search")
    print("3) Exit")
    user_choice = int(input(
        "Please choose an option for type of search you want the program to use: "))
    if user_choice == 1:
        guess_random_num_linear(tries, start, stop)
    elif user_choice == 2:
        guess_random_num_binary(tries, start, stop)
    elif user_choice == 3:
        return
    else:
        print("Invalid entry")
        ask_user(tries, start, stop)


ask_user(5, 0, 10)
