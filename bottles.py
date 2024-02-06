beverage = "Capri Sun"
count = 99
for i in range(99,1,-1):
    print(count, "bottles of", beverage, "on the wall")
    print(count, "bottles of", beverage)
    print("Take one down, pass it around")
    count = count - 1
    print(count, "bottles of", beverage, "on the wall")

    print("")
    
    if count == 5:
        print(count, "bottles of", beverage, "on the wall")
        print(count, "bottles of", beverage)
        print("If one of these bottles should happen to fall,",count-1, "bottles of",beverage, "on the wall")
        count = count - 1
    
    print("")

print("We're out of bottles of", beverage)
print("Hopefully everyone had fun, because we're just getting started!")