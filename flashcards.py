import random

flashcards = [("What is a name that refers to a value?", "variable"),
              ("What is a value that is passed to a function called?","argument"),
              ("What is a statement that assigns a value to a variable?","assignment"),
              ("What is a combination of variables operators and values that represents a single result?","expression"),
              ("What is it called to simplify an expression by performing the operations in order to get a single value","evaluate"),
              ("What is it called to run a statement and do what it says","execute"),
              ("What is a unit of code that has an effect like creating a variable or displaying a value?","statement"),
              ("What is a data type that indicates values are whole numbers?","integer"),
              ("What data type is a number with decimal points?","float"),
              ("What data type is text values","string")]

random.shuffle(flashcards)

user_answer=""

print("Hello and welcome to the flashcard program!")
print("Enter 1 to see the answer and 2 to exit.")

for question, answer in flashcards:
    while user_answer!="2":
        print(question)
        user_answer = input("What is your answer? ")
        
        if user_answer.lower() == "1":
            print("Here is the answer")
            print(answer)
            print("Next question")
            print("")
            break

        elif user_answer=="2":
            print("Exiting program")

            break
        elif user_answer.lower() == answer:
            print("Correct!")
            print("")
            break
        
        elif print("Wrong try again"):
            user_answer=input("").lower()