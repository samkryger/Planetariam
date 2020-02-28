from Planet import Planet

mercury = Planet("Mercury" ,"First planet from the sun")
venus = Planet("Venus", "Second planet from the sun")
earth = Planet("Earth", "Big Blue")
mars = Planet("Mars", "Red Color")
jupiter = Planet("Jupiter", "Gas Giant")
saturn = Planet("Saturn", "6th planet from the sun")
uranus = Planet("Planet", "Has a funny name")
neptune = Planet("Neptune", "Gas Giant with extremely cold temperatures")

def menu():
    print("Here are your options: ")
    print("1 - Mercury")
    print("2 - Venus")
    print("3 - Earth")
    print("4 - Mars")
    print("5 - Jupiter")
    print("6 - Saturn")
    print("7 - Uranus")
    print("8 - Neptune")
    print("Q - Quit")

menu()
choice = input("What do you want to do?: ")

while(choice != 'Q'):
    if(choice == '1'):
        print("You chose Mercury!:")
        print(str(mercury))
    elif(choice == '2'):
        print("You chose Venus!:")
        print(str(venus))
    elif(choice == '3'):
        print("You chose Earth!:")
        print(str(earth))
    elif(choice == '4'):
        print("You chose Mars!:")
        print(str(mars))
    elif(choice == '5'):
        print("You chose Jupiter!:")
        print(str(jupiter))
    elif(choice == '6'):
        print("You chose Saturn!:")
        print(str(saturn))
    elif(choice == '7'):
        print("You chose Uranus!:")
        print(str(uranus))
    elif(choice == '8'):
        print("You chose Neptune!:")
        print(str(neptune))
    else:
        print("Oops, I do not know what you are looking for.")
    menu()
    choice = input("What do you want to do?")
print("Have a good one")
