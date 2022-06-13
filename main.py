import random 

print("Welcome!!\nThis is a Rock-Paper-Scissors Game")

list_of_options = ['R','P','S']

print("'R' represents Rock\n'P' represents Paper\n'S' represents Scissors")

user_input = input("Pick an option (R, P, S): ")

wrong_input = True

while wrong_input:
    if user_input.upper() in list_of_options:
        break

    else:
        print("Error! You've entered a wrong input. Please try again")    
        user_input = input("Pick an option (R, P, S): ")        

if user_input.upper() == "R":
    user_input = "Rock"

elif user_input.upper() == 'P':
    user_input = 'Paper'

elif user_input.upper() == 'S':
    user_input = 'Scissors'
    

for i in range(len(list_of_options)):
    if list_of_options[i] == 'R':
        list_of_options[i] = 'Rock'

    if list_of_options[i] == 'P':
        list_of_options[i] = 'Paper'

    if list_of_options[i] == 'S':
        list_of_options[i] = 'Scissors'


cpu_option = random.choice(list_of_options)

print("Player (" + user_input + ") : CPU (" + cpu_option + ")")

a_tie = True
while a_tie:
    if user_input != cpu_option:
        break
    
    elif user_input == cpu_option:
        print("Both palyers selected ", user_input ,". It is a tie!")
        user_input = input("Pick an option (R, P, S): ")

        list_of_options = ['R','P','S']
        
        wrong_input = True    

        while wrong_input:
            if user_input.upper() in list_of_options:
                break

            else:
                print("Error! You've entered a wrong input. Please try again")    
                user_input = input("Pick an option (R, P, S): ") 

        if user_input.upper() == "R":
            user_input = "Rock"

        elif user_input.upper() == 'P':
            user_input = 'Paper'

        elif user_input.upper() == 'S':
            user_input = 'Scissors'    

        for i in range(len(list_of_options)):
            if list_of_options[i] == 'R':
                list_of_options[i] = 'Rock'

            if list_of_options[i] == 'P':
                list_of_options[i] = 'Paper'

            if list_of_options[i] == 'S':
                list_of_options[i] = 'Scissors'

        cpu_option = random.choice(list_of_options)

        print("Player (" + user_input + ") : CPU (" + cpu_option + ")")    

if user_input == "Rock":
    if cpu_option == "Scissors":
        print("Rock smashes Scissors! You win!")
    else:
        print("Paper covers Rock! You lose!")

elif user_input == "Paper":
    if cpu_option == "Rock":
        print("Paper covers Rock! You win!")
    else:
        print("Scissors cuts Paper! You lose!")
        
elif user_input == "Scissors":
    if cpu_option == "Paper":
        print("Scissors cuts Paper! You win!")
    else:
        print("Rock smashes Scissors! You lose!")