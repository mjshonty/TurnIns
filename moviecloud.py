# api key - you'll need your own API key from https://www.themoviedb.org/ 
api_key = ""

# Imported modules we'll need
from turtle import *
import requests
import json
#from pprint import pprint

# base URL for accessing the TMBD API
movies_base= "https://api.themoviedb.org/3/"


# additional URLS for searching
movie_search = movies_base + "search/movie"

# get user input for movie 
search_query = textinput("Movie Search", "What movie would you like to search for? ")

# movie search query
parameter = {"api_key": api_key, "query":search_query}

# search movies and store off the results
search_results_json = requests.get(movie_search, parameter)

# result loaded into dictionary
search_results = json.loads(search_results_json.text)

# parameter to be used for searching when looking for the cast of the movie
parameter2 = {"api_key": api_key}

# turtle settings 
screen = Screen()
screen.bgcolor("sky blue")
speed(0)

def cloud_part(radius):
    color("white","white")
    begin_fill()
    circle(radius)
    end_fill()

def draw_cloud(radius):
    cloud_part(radius)
    forward(radius)
    cloud_part(radius)
    right(90)
    cloud_part(radius)
    right(90)
    cloud_part(radius)
    right(90)
    cloud_part(radius)
    right(90)

radius = 50

# function to get the first result from the user's movie search, draw the title, and return the movie ID
def user_search(search_results1):
    top_movie = 0 # counter to only grab top movie
    for titles in search_results1['results']: # loop through the search results list on the results dictionary
        top_movie = top_movie + 1 # set top movie to 1 to only grab the first movie
        movie_title = titles["title"] # set the movie tittle to the first title in the title dictionary
        penup()
        goto(x=-350, y=200)
        write(movie_title, align="left", font=("impact", 60, "bold"), move=True) #write the movie title
        movie_id = str(titles['id']) # get the movie id from the titles dictionary as a string and assign it
        if top_movie == 1: # break the loop after getting the first title
            break
    return movie_id # return the movie id for use elsewhere

# function to take movie id and get cast to return as a list
def actor_list(movie_credits_dict): 
    top_10 = 0 # counter for the number of times we loop
    actors = [] # list to store off top 10 actors
    for cast in movie_credits_dict["cast"]: # loop through entries in the cast dictionary
        top_10 = top_10 +1 # keep track of the number of loops
        actors.append(cast["name"]) # append the top words to the list
        # del movie_credits_dict[cast] ### can use this in loop to remove entry from dictionary and then pass the dicionary back in to get the next 5 words to draw at a different size
        if top_10 == 10: # stop the loop after getting 10 actors
            break
    return actors # return the list of actors

# function to draw actors
def draw_actors(actors):
    penup()
    goto(x=-350, y=100)
    for actor in actors: # for actor in the actors list do the following drawings
        color("#4d4d4d")
        write(actor, align="left", font=("futura", 30, "normal"), move=True)
        setx(-350)
        right(90)
        forward(40)
        left(90)

# stores of the movie id
movie_id = user_search(search_results) 


# storing of string to pass into search
movie_credits = movies_base + "movie/" + movie_id + "/credits" 

# search credits and store off the results
movie_credits_json = requests.get( movie_credits, parameter2)

# search result loaded into python dictionary format
movie_credits_dict = json.loads(movie_credits_json.text)


actors = actor_list(movie_credits_dict)


draw_actors(actors)
goto(250,100)
draw_cloud(radius)
right(90)
forward(300)
draw_cloud(radius)
done()