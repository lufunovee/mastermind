import random


# TODO: Decompose into functions
code = ""
answer = ""
turns = 0
correct = False
correct_digits_and_position = 0
correct_digits_only = 0
def generate_code():
    """
    generating the code the user is supposed to guess
    """
    global code
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

    # print(code)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    

def check_user_input():
    """
    checking if input is not more than 4 or less than 4
    """
    global answer
    
    while True:
        answer = input("Input 4 digit code: ")
        
        if len(answer) < 4 or len(answer) > 4 or answer.isdigit()==False or \
            all(int(x)in range(1,9) for x in answer ) == False :
            print("Please enter exactly 4 digits.")
            continue
        else :
            break
            

def check_correct_digit(): 
    """
    checking how many digits are correct and not in the corect place 
    and how many are in the correct place  
    """
    global turns,correct_digits_and_position ,correct_digits_only
      
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
                correct_digits_only += 1

    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    turns += 1


def number_of_digits():
    """
    checking the if the user input is exactly the same as the code generated
    """
    global correct


    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
        #'The code was: '+str(code))
        
    else:
        print('Turns left: '+str(12 - turns))
    

   
def run_game():
    global code
    code = [0,0,0,0]
    
    generate_code()
    while  turns < 12:
        check_user_input()
        check_correct_digit()
        number_of_digits()
        if correct:
            break
    print('The code was: '+str(code))    


if __name__ == "__main__":
    run_game()
