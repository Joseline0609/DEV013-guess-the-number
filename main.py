"""Module providing a function printing python version."""

import random
import pyfiglet


def saludar():
    """function to print a welcome message using pyfigley library to costumize it"""
    ascii_art = pyfiglet.figlet_format("¡Bienvenida!")
    print(ascii_art)
    print("Intenta adivinar un número entre 1 y 100.")

saludar()

def generate_random_number ():
    """function to generate a random number to  call when necessary"""
    return random.randint(1, 100)

def validate_user_inputs(secret_number, conjecture):
    """function to validate if the conjectures are equal to the secret number"""
    message = ""

    if conjecture < secret_number:
        message += "Demasiado bajo:("
    elif conjecture>secret_number:
        message += "Demasiado alto:("
    else:
        message += "¡Felicidades!:) ¡Adivinaste el número!"

    customize_message= pyfiglet.figlet_format(message, font="digital")
    return customize_message

def validate_computer_number(secret_number, conjecture):
    """function to validate if the numbers generated are equal to the secret number"""
    message = ""

    if conjecture < secret_number:
        message += "Muy bajo:("
    elif conjecture>secret_number:
        message += "Muy alto alto:("
    else:
        message += "¡Tu oponente ha adivinado el numero!"

    return message


def play_again():
    """function to restart the game"""
    response = input("Quieres juegar nuevamente? y/n")
    print(response)
    if response == "y":
        game()
    else:
        print("Vuelve Pronto:)")

def game():
    """game logic"""
      # generate the secret number
    SECRET_NUMBER = generate_random_number()
      # variable to save the user conjectures
    user_conjectures = []
    computer_conjectures = []

    while True:
        # variable to save the user input and convert it into an intenger
        user_conjecture = int(input("Qué número eliges?"))
        message = validate_user_inputs(SECRET_NUMBER, user_conjecture)
        print(message)
        # add the user conjecture to the list
        user_conjectures.append(user_conjecture)

        if user_conjecture == SECRET_NUMBER:
        # print the user conjectures into the terminal
            print(f"Tus intentos fueron: {user_conjectures}")
            break

        computer_conjecture = generate_random_number()
        print(f"La computadora adivinó: {computer_conjecture}")
        message = validate_computer_number(SECRET_NUMBER, computer_conjecture)
        print(message)
        computer_conjectures.append(computer_conjecture)

        if computer_conjecture == SECRET_NUMBER:
            print(f"Sus intentos fueron: {computer_conjectures}")
            break

def execute_game():
    """To reload the game"""
    game()
    play_again()


if __name__ == "__main__":
    execute_game()
