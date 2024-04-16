import sys
from turtle import *
speed(0)

### My attempt to be clever and user the a list of 100 of the most common words to set our stop list. Removing certain words ends up causing spacing issues when drawing with turtle.

def stop_words_source(): # look to list of 100 most common english words and add as a string to a variable.
    with open("stop_words.txt", "r", encoding="utf-8") as l:
        stop_word_list = ""
        for line in l:
            stop_word_list = stop_word_list + line
        return stop_word_list

def stop_word_list(words_list): # pass in variable containing the string of stop words and split them into a list
    stop_words_used = words_list.split() #words are already lowercase and do not contain any punctuation so they only need to be put in a list
    return stop_words_used

stop_words_to_use = stop_words_source()
stop_words = stop_word_list(stop_words_to_use) #stop word list from stop_words.txt using above functions.

# stop_words = ['i',"and", "of", "to", "a", "the" ]

def file_to_use(file_name): # function to take in file name from user
   words_list = ""
   with open(file_name, "r", encoding = "utf-8") as f: # filename, Read or Write, encounding to avoid funny characters
        line = f
        for line in f:
            words_list = words_list + line
        return words_list

def total_words(words_list): # sets all the words to lower case, strips out non-letter characters, and puts them all in a list
    words_list =words_list.lower()
    words_list = words_list.replace("\n", " ")
    words_list = words_list.replace(",", " ")
    words_list = words_list.replace(".", " ")
    words_list = words_list.replace(":", " ")
    words_list = words_list.replace(";", " ")
    total_words = words_list.split()
    return total_words


def count_words(words_list): # counts how many times a word appears in the list and stores it as a key:value pair in a dicationary
    words_dict = {}
    for word in words_list:
        if word not in stop_words: # only adds words that are not in the stop_words list
            words_dict.setdefault(word, 0)
            words_dict[word] = words_dict[word] + 1
    return words_dict

def count_words2(words_list): # counts how many times a word appears in the list and stores it as a key:value pair in a dicationary
    words_dict = {}
    for word in words_list:
        words_dict.setdefault(word, 0)
        words_dict[word] = words_dict[word] + 1
    return words_dict

def sort_frequency(word_dictionary): # sorts how frequently a word appears by checking the value of each key
    top_3 = 0 # counter for the number of times we loop
    top_words = [] # list to store off the top words
    for key in sorted(word_dictionary, key=word_dictionary.get, reverse=True):
        top_3 = top_3 +1 # keep track of the number of loops
        top_words.append(key) # append the top words to the list
        del word_dictionary[key] ### can use this in loop to remove entry from dictionary and then pass the dicionary back in to get the next 5 words to draw at a different size
        if top_3 == 3: # stop the loop after the specified number
            break
    return top_words # return a list of the top words for use with turtle



def draw_words_h1(top_words):
    penup()
    goto(x=-400, y=-90)
    for word in top_words:
        color("#920707")
        write(word, align="left", font=("Rockwell", 100, "bold"), move=True)
        right(90)
        forward(110)
        left(90)

def draw_words_h2(top_words):
    penup()
    goto(x=-225, y=0)
    for word in top_words:
        color("#BA2424")
        write(word, align="left", font=("Rockwell", 60, "bold"), move=True)
        right(90)
        forward(60)
        left(90)

def draw_words_h3(top_words):
    penup()
    goto(x=-100, y=100)
    for word in top_words:
        color("#DB5454")
        write(word, align="left", font=("Rockwell", 40, "normal"), move=True)
        right(90)
        forward(40)
        left(90)

def draw_words_h4(top_words):
    penup()
    goto(x=-25, y=180)
    for word in top_words:
        color("#E07E7E")
        write(word, align="left", font=("Rockwell", 30, "normal"), move=True)
        right(90)
        forward(30)
        left(90)

def draw_words_h5(top_words):
    penup()
    goto(x=-10, y=225)
    for word in top_words:
        color("#E9B1B1")
        write(word, align="left",font=("Rockwell", 20, "normal"), move=True)
        right(90)
        forward(20)
        left(90)
    hideturtle()


file_name = sys.argv[1] # ask the user to specify a specific file

words_list = file_to_use(file_name)



list_of_words = total_words(words_list)
word_list_dict = count_words(list_of_words)
words_to_draw = sort_frequency(word_list_dict)
draw_words_h1(words_to_draw)
words_to_draw = sort_frequency(word_list_dict)
draw_words_h2(words_to_draw)
words_to_draw = sort_frequency(word_list_dict)
draw_words_h3(words_to_draw)
words_to_draw = sort_frequency(word_list_dict)
draw_words_h4(words_to_draw)
words_to_draw = sort_frequency(word_list_dict)
draw_words_h5(words_to_draw)

done()