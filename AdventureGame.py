print("Your a whiz bomb defuser have been called upon to disarm a the biggest time bomb you've ever encountered that will destroy a half the city if not defused fast enough. The timer is counting down fast.")

print("")

answer = input ("There are two wires that look like they would disarm the bomb, a [red] and [blue] wire. Which do you cut?").lower()

if answer =="red":
    print("You clip the red wire, the timer turns off. You hear a few beeps before everything turns to black.")
    print("")
   
    answer = input("You hear a voice telling you not to give up. Do you [get up] or heads towards the [light]?").lower()
    if answer == "get up":
            print("You've got one more shot.")
            print("")

            answer = input("Alright kid, what will it be now? [green] or [blue]?").lower()
            if answer == "green":
                print("There isn't a green wire! Shoulda left you dead")
                print("Waste of a miracle. Ending 1/7")
            
            elif answer == "blue":
                  print("Good job kid, you saved the city!")
                  print("Second chances. Ending 2/7")
            else:
                  print("What are you doing?! I guess you want to die again?")
                  print("Glutton for punishment. Ending 3/7")

    elif answer == ("light"):
            print("Guess you'll be answering for your failings at the pearly gates.")
            print("Knockin' on heavens' door. Ending 4/7")
    else:
            print("Couldn't pull yourself back together, huh?")
            print("I've fallen and I can't get up. Ending 5/7")

elif answer == "blue":
    print ("You clip the blue wire. The timer stops with 1 second left. You breath a sigh of relief and get to go home one last time.")
    print("Cool under pressure. Ending 6/7.")
else:
    print("You ran out of time. The bomb is going to explode!")
    print("Indecisive. Ending 7/7.")