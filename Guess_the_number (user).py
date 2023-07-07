import random


def computer_guess(x):
    low = 1
    high = x
    user_choice = ''
    count = 0
    print('Hey this is user XYZ and my number is 12!')
    print('Hey! This is computer to which you are staring right now lol!')
    print('I am gonna guess your number! Shall we begin! Lets Go')
    while user_choice != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # because if high and low are same ie 1 guess=1

        user_choice = input(
            f'Is {guess} too high(H), too low(L), correct(c)? ')
        user_choice = user_choice.lower()

        if user_choice == 'h':
            high = guess-1

        elif user_choice == 'l':
            low = guess+1

        elif user_choice == 'c':
            print(
                f'Yayy! The computer guessed your number,{guess}, correctly in {count+1} steps.')

        else:
            print('INVALID PROMPT! ENTER h / l / c only!!')

        count = count+1


computer_guess(20)
