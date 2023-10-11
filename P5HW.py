# CTI-110
# P5HW - Math Quiz
# name redacted
# 10/11/2023
# This program asks for an input mode. If the mode is 1, the program throws 2 random numbers and asks for the sum of the numbers.
# If the answer is false, the program hints at whether the answer was greater than or less than the correct answer.
# Else, the program congratulates the user and returns back to the menu.
# Next, if the mode is 2, the program throws 2 random numbers and asks for the result of the first number minus the second number, with the same logic as above.
# Finally, if the mode is 3, the program terminates.

import random

def throw_two_integers() -> tuple[int, int]:
    return (random.randint(1, 100), random.randint(1, 100))


def show_menu() -> None:
    print("\nMAIN MENU\n--------------------\n1. Adding Random Numbers\n2. Subtracting Random Numbers\n3. Exit\n")


def is_answer_correct(_attempt: int, _correct: int) -> bool:
    is_correct = _attempt == _correct

    if not is_correct:
        if _attempt < _correct:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

    return is_correct


def throw_addition():
    int_1, int_2 = throw_two_integers()
    input_string = "\nEnter answer.\n"
    
    print(f"  {int_1}")
    print(f"+ {int_2}")
    
    correct_answer = int_1 + int_2
    number_of_guesses = 1
    attempt = int(input(input_string))
    
    while not is_answer_correct(attempt, correct_answer):
        input_string = "\nTry again: "

        attempt = int(input(input_string))
        number_of_guesses += 1

    print("Congratulations!!!! Your answer is correct.")
    print("Number of guesses:", number_of_guesses)

    show_menu()


def throw_subtraction():
    int_1, int_2 = throw_two_integers()
    input_string = "\nEnter answer.\n"
    
    print(f"  {int_1}")
    print(f"- {int_2}")
    
    correct_answer = int_1 - int_2
    number_of_guesses = 1
    attempt = int(input(input_string))
    
    while not is_answer_correct(attempt, correct_answer):
        input_string = "\nTry again: "

        attempt = int(input(input_string))
        number_of_guesses += 1

    print("Congratulations!!!! Your answer is correct.")
    print("Number of guesses:", number_of_guesses)

    show_menu()


print("Welcome to Math Quiz\n")
show_menu()

menu_mode = int(input("Please choose one of the menu options: "))
while menu_mode != 3:
    
    if menu_mode == 1:
        throw_addition()
    elif menu_mode == 2:
        throw_subtraction()

    menu_mode = int(input("Please choose one of the menu options: "))

print("Thank you for playing...\nBye!!")
