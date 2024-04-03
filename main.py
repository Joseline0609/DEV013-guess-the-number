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

def validate_inputs(secret_number, conjecture):
    """function to validate if the conjectures are equal to the secret number"""
    if conjecture < secret_number:
        menssage_low = pyfiglet.figlet_format("Demasiado bajo:(", font="digital")
        print(menssage_low)
        return menssage_low
    elif conjecture>secret_number:
        message_high = pyfiglet.figlet_format("Demasiado alto:(", font="digital")
        print(message_high)
        return message_high
    else:
        winner_message = "¡Felicidades!:) ¡Adivinaste el número!"
        print(winner_message)
        play_again()
        return winner_message

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

    while True:
        # variable to save the user input and convert it into an intenger
        user_conjecture = int(input("Qué número eliges?"))
        validate_inputs(SECRET_NUMBER, user_conjecture)
        # add the user conjecture to the list
        user_conjectures.append(user_conjecture)

        if user_conjecture == SECRET_NUMBER:
        # print the user conjectures into the terminal
            print(f"Tus intentos fueron: {user_conjectures}")
            break

        computer_conjecture = generate_random_number()
        print(f"La computadora adivinó: {computer_conjecture}")
        validate_inputs(SECRET_NUMBER, computer_conjecture)
        user_conjectures.append(user_conjecture)

        if computer_conjecture == SECRET_NUMBER:
            print(f"Tus intentos fueron: {user_conjectures}")
            break


if __name__ == "__main__":
    game()
