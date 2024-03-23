import sys
from turtle import *

##solution = "mississippi"
##num_letters = len(solution)
##in_progress = list( '_'*num_letters )
##write(in_progress, font=('Arial',16))

def guess_check(guess): #function checks if the user's guess is in the solution list and returns yes or no
    if guess in solution:
       answer = "yes"
       return (answer)
    else:
       answer = "no"
       return (answer)

def user_guess(): #function asks the user for input and returns it for assignment to a variable
    guess = input("What is your guess?  ")
    ##guess = textinput("your guess", "What is your guess?  ")
    if guess == "":
        sys.exit()
    return(guess)

def letter_places(word, letter): #function takes the word to guess locates what position the letters are in then compares the users input to find out what position the guess is in
    places = []
    start = 0
    while True:
        where = word.find(letter,start)
        if (where == -1):
            break
        places.append(where)
        start = where + 1
    return places

def draw_letter(places, userguess):
    if places == [0]:
        write(userguess)
    else:
        write(userguess)

def subract_guess(userinput):
    remaining = 5
    if userinput == "no":
        remaining = -1
        return (remaining)
    else:
        return (remaining)

def guess_word():
    word = "Arrakis"
    word = word.lower()
    return (word)


def solution_list(word):
    solution = [] #empty list that will contain all the letters of the word to guess
    for letters in word: #loop on all the letters in the word to guess
        solution.append(letters) #add the letters from the word to guess into the list called solution
    return solution
word = guess_word()    

solution = solution_list(word)

rguesses = 5 #give the user a total of 5 guesses

while rguesses != 0: #while the user hasn't used all their guesses
    uguess = user_guess() #get the user's input and set uguess to that value
    letter_exists = guess_check(uguess) #pass in the user's guess to the guess_check function to find out if their guess is in the solution list - set letter exists to yes or no
    places = letter_places(word, uguess) #check their guess against the word and locate what positions of the word their letter is in set that value to places
    
    if letter_exists == "yes": #if the value in the variable is yes
        print("That's correct!") #print a message letting the user know they're correct
        dplaces = places
        #call function to draw the letters we should be able to use value in places to know where to draw letter
    else: #if the the value of variable is no
        rguesses = rguesses + subract_guess(letter_exists) #set the reamining_guesses variable to itself - 1 so that we use up a guess
        if rguesses == 0: #once we have 0 guesses remaining
            print("You lose") #tell the user they've lost and close the game
        else: #if they still have guesses remaining
            print("you can only get "+ str(rguesses) + " more wrong answers") #Let the user know they only have so many wrong guesses left
            dplaces = places
            #call function to draw whatever parts of the hangman need to be drawn based on value in guesses_reamining
            #call function to show guessed letter based on value in uguess

        
    