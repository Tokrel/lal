import random

tärningar = input("Hur många tärningar behövs i spelet? ")
kast = input("Hur många kast får en spelare? ")

tärningar = int(tärningar)
kast = int(kast)-1

keep = 1
while True:
    mylist = []
    press = input("Genom att trycka på Enter kan du börja kasta. Om du vill avsluta skriv 'a': ")
    if press == "a":
        print("Tack och hej!")
        break
    else:
        for i in range(tärningar):
            nummer = random.randint(1, 6)
            print("Tärning", i + 1, ":", nummer)
            mylist.append(str(nummer))  # Use append to add the number to the list
        
        if kast > 0:
            omgång = 0
            while omgång < kast:
                kastalgen = input("Är du inte nöjd kan du kasta igen. Vill du kasta igen (j/n)? ")
                if kastalgen == "j":
                    mylist = []  # Clear the list before the next roll
                    for i in range(tärningar):
                        nummer = random.randint(1, 6)
                        print("Tärning", i + 1, ":", nummer)
                        mylist.append(str(nummer))
                        omgång = omgång+1
                        
                 
                elif kastalgen == "n":
                  
                    break
                else:
                    print("Ogiltigt val. Försök igen.")
        print("Du fick", ", ".join(mylist) + ".")

