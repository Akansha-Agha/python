import random 
def generate_number():
    "This function helps to generate a random number between 1 to 100"
    number = random.randint(1,100)
    return number

def check_the_guess (number,user_guess):
    """
    This function helps to check whether a user guess is 
    equal,lower or higher than the random number generated.
    """
    
    if(number == int(user_guess)):
        print("Your guess is correct !! ")
    elif (number < int(user_guess)):
        print("Your Guess is greater than the original number.")
    elif (number > int(user_guess)):
        print("Your number is lower than the original number .")

def validate_guess(user_guess):
    """
    The function checks whether the number is an integer.
    Returns true if the number is an integer otherwise, false.
    """
    if user_guess.isdigit():
        if int(user_guess)>=1 and int(user_guess)<=100:
            return True
    else:
        return False

def play_game():
    "The main game with which the user interacts."
    original_num = generate_number() #the random number generated
    valid_guess = False #A flag to check whether the user guess is vaid

    while valid_guess == False :    #Continues until the user guess is an integer.
        print("Guess a number between 1 to 100 :")
        user_input = input() 

        if validate_guess(user_input) == True:
            user_input = int(user_input)
            check_the_guess(original_num,user_input)
            valid_guess = True
        else:
            print("invalid input. Try again")

play_game()
