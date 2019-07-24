###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you


def guess_game():
    import random
    digits = list(range(10))
    random.shuffle(digits)
    the_list = digits[:3]
    print(the_list)

    solved = False

    # keep get guesses untill solve it
    while solved == False:
        match = 0
        close = 0
        nope = 0
        guess_list = get_a_guess()
        print(guess_list)
        # if the guess equal the list
        if guess_list == the_list:
            print('Congratulations, you solve it!')
            solved = True
            return 'Solved'
        else:
            for i in range(len(the_list)):
                if guess_list[i] == the_list[i]:
                    match+=1
                elif guess_list[i] in the_list:
                    close+=1
                else:
                    nope+=1
            print('You have {} match, {} close, {} not in the list...'.format(match, close, nope))

                
        



def get_a_guess():
    guess = input("What is your guess? ")
    guess_list = list(map(int, guess))
    return guess_list


guess_game()





# Another hint:
# guess = input("What is your guess? ")
# guess_list = list(map(int, guess))
# print(guess_list)
# if the_list == guess_list:
#     print('Great! you gess it....')

# for i in the_list:
#     if i in guess:
#         if 
# # 234




# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
