import sys
from turtle import *

speed(6)

#screen=Screen()
#screen.setup(width=1000, height=2000) 


#draw gallows function
def gallows():
    #draw the base
    penup()
    goto(-400, -300)
    pendown()
    forward(600)
    left(90)
    forward(25)
    left(90)
    forward(600)
    left(90)
    forward(25)
    left(90)
    left(90)
    #draw the vertical post
    forward(600)
    right(90)
    forward(25)
    right(90)
    forward(575)
    right(90)
    forward(25)
    right(90)
    penup()
    #draw the horizontal post
    forward(600)
    pendown()
    right(90)
    forward(450)
    right(90)
    forward(25)
    right(90)
    forward(450)
    right(90)
    forward(25)
    right(90)      

#draw rope
def rope():
    right(90)
    forward(25)
    left(90)
    forward(300)
    right(90)
    forward(75)
    
#draw head
def head():
    penup()
    right(90)
    forward(10)
    pendown()
    circle(40)

#draw body
def body():
    penup()
    left(90)
    forward(80)
    pendown()
    right(90)
    forward(40)
    left(90)
    forward(120)
    left(90)
    forward(80)
    left(90)
    forward(120)
    left(90)
    forward(40)
    
#draw left arm
def left_arm():
    penup()
    forward(40)
    left(90)
    forward(20)
    pendown()
    right(50)
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(90)
    left(50)
    forward(20)
    penup()

#draw right arm
def right_arm():
    penup()
    forward(20)
    right(90)
    forward(80)
    right(90)
    forward(20)
    pendown()
    left(50)
    forward(100)
    right(90)
    forward(10)
    right(90)
    forward(90)
    right(50)
    forward(20)
    penup()

#draw right leg
def right_leg():
    left(180)
    forward(110)
    right(90)
    forward(20)
    pendown()
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)
    forward(100)
    penup()
    
#draw left leg
def left_leg():
    left(90)
    forward(20)
    left(90)
    pendown()
    forward(100)
    right(90)
    forward(10)
    right(90)
    forward(100)


#draw letters function
t = Turtle()
t2 = t.clone()
def setup_correct_letter():#goes to top of screen to draw correct guesses
    t2.penup()
    t2.goto(x=-400, y=400)
    t2.pendown()

def draw_correct_letter():#rewrites the correct guesses line to show any updated correct guesses
    t2.clear()
    t2.write(progress, font=("Arial", 40, "normal"))
  

#draw incorrect letters function
def draw_incorrect_letter():#not sure how to get this to work, want it to write incorrect letters at bottom
    t4 = t.clone()
    t4.penup()
    t4.goto(x=-400, y=-400)
    t4.pendown()
    t4.write("these are incorrect letters", font=("Arial", 20, "normal"))
    t4.penup()


def thats_correct():#I can it this to write but it stays in the corner even if a user gets it wrong
    t7 = t.clone()
    t7.penup()
    t7.goto(x=200, y=400)
    t7.pendown()
    t7.write("That's correct!", font=("Arial", 20, "normal"))

    


def guess_check(guess): #function checks if the user's guess is in the solution list and returns yes or no
    if guess in solution:
       answer = "yes"
       return (answer)
    else:
       answer = "no"
       return (answer)

def user_guess(): #function asks the user for input and returns it for assignment to a variable
    guess = textinput("Enter guess", "What is your guess?").lower()
    ##guess = textinput("your guess", "What is your guess?  ")
    if guess == "exit":
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

Drawsolution = "Arrakis"
num_letters = len(Drawsolution)
in_progress = list('_'*num_letters)
progress =','.join(in_progress)

word = guess_word()    
solution = solution_list(word)
remaining_guesses = 5 #give the user a total of 5 guesses


gallows()
rope()
setup_correct_letter()


while remaining_guesses != 0: #while the user hasn't used all their guesses
    uguess = user_guess() #get the user's input and set uguess to that value
    letter_exists = guess_check(uguess) #pass in the user's guess to the guess_check function to find out if their guess is in the solution list - set letter exists to yes or no
    if uguess is None:
        break
    places = letter_places(word, uguess) #check their guess against the word and locate what positions of the word their letter is in set that value to places
    if letter_exists == "yes": #if the value in the variable is yes
       for place in places: #
            in_progress[place] = uguess
            progress = ','.join(in_progress)
            draw_correct_letter()
        #call function to draw the letters we should be able to use value in places to know where to draw letter
    else: #if the the value of variable is no
        remaining_guesses = remaining_guesses + subract_guess(letter_exists) #set the reamining_guesses variable to itself - 1 so that we use up a guess
        if remaining_guesses == 4:
            head()
            body()
        elif remaining_guesses == 3:
            left_arm()
        elif remaining_guesses == 2:
            right_arm()
        elif remaining_guesses == 1:
            right_leg()
        elif remaining_guesses == 0: #once we have 0 guesses remaining
            left_leg()
            print("You lose") #tell the user they've lost and close the game
        else: #if they still have guesses remaining
            print("you can only get "+ str(remaining_guesses) + " more wrong answers") #Let the user know they only have so many wrong guesses left
            dplaces = places
            #call function to draw whatever parts of the hangman need to be drawn based on value in guesses_reamining
            #call function to show guessed letter based on value in uguess

done()