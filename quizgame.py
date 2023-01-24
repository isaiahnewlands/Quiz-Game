print("Welcome to my computer quiz!")

playing = input("Do you want to play?" )

if playing != "yes":
    quit()
    
print("Okay! Letye's play :)")

answer = input("what does CPU stand for? ")
if answer == "Central Processing Unit":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What year did the olympics begin? ")
if answer == "1899":
    print("Correct!")
else:
    print("Incorrect")

answer = input("What indie game developer spawned a horror game franchise known as Five Nights At Freddys")
if answer == "Scott Cawthon":
    print("Correct!")
else:
    print("Incorrect")