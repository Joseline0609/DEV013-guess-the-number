import random
import pyfiglet

# function to print a welcome message using pyfigley library to costumize it 
def saludar():
    ascii_art = pyfiglet.figlet_format("¡Bienvenida!")
    print(ascii_art)
    print("Intenta adivinar un número entre 1 y 100.")

saludar()

# function to generate a random number to  call when necessary
def generate_random_number ():
  return random.randint(1, 100)

# function to validate if the conjectures are equal to the secret number
def validate_inputs(secret_number, conjecture):
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
   
# function to restart the game 
def play_again():
  response = input("Quieres juegar nuevamente? y/n")
  print(response)
  if response == "y":
    game()
  else:
    print("Vuelve Pronto:)")

# function to save the user inputs 
def save_user_conjecture(new_conjecture, array):
    array.append(new_conjecture)
    return array


# game logic
def game():
  # generate the secret number
  SECRET_NUMBER = generate_random_number()
  # variable to save the user conjectures
  user_conjectures = []

  while True:
   # variable to save the user input and convert it into an intenger
   user_conjecture = int(input("Qué número eliges?"))
   validate_inputs(SECRET_NUMBER, user_conjecture)
   # add the user conjecture to the list
   save_user_conjecture(user_conjecture, user_conjectures)

   if user_conjecture == SECRET_NUMBER:
    # print the user conjectures into the terminal
    print(f"Tus intentos fueron: {user_conjectures}")
    break
   
   computer_conjecture = generate_random_number()
   print(f"La computadora adivinó: {computer_conjecture}")
   validate_inputs(SECRET_NUMBER, computer_conjecture)

   if computer_conjecture == SECRET_NUMBER:
    print(f"Tus intentos fueron: {user_conjectures}")
    break
   

if __name__ == "__main__":
    game()