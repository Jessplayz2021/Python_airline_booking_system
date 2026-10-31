import time
from datetime import date

today = date.today()
d1 = today.strftime("%d")
m1 = today.strftime("%m")
y1 = today.strftime("%Y")
D1=int(d1)
M1=int(m1)
Y1=int(y1)

def goto(linenum):
    global line
    line = linenum
line = 3 
while True:
    if line == 3:
        FIRSTNAME = input("Please enter your first name: ")
        SURNAME = input("Please enter your surname: ")
        AGE = int(input("Please enter your age: "))
        DATEOFBIRTHDAY = int(input("Please input the day you was born in: "))
        DATEOFBIRTHMONTH = int(input("Please input the month that you was born in (Please input as numbers): "))
        DATEOFBIRTHYEAR = int(input("Please input the Year that you was born in (as YYYY): "))
        LUGGAGEPACK = input("Have you packed you luggage (yes.no.N/A)? ")
        NUMBEROFBAGS = int(input("Please enter your number of bags (if you answered N/A put 0): "))
        AGEMONTH=M1-DATEOFBIRTHMONTH
        AGEDAY=D1-DATEOFBIRTHDAY
        AGEYEAR=Y1-DATEOFBIRTHYEAR
        AGE2=AGE+1
        UPPERLUGGAGEPACK = LUGGAGEPACK.upper()
        if UPPERLUGGAGEPACK == "YES":
            print("Okay, you may continue.")
            goto(4)
        elif UPPERLUGGAGEPACK == "NO":
            print("You cannot board with us")
            goto(3)
        elif UPPERLUGGAGEPACK == 'N/A':
            print("Thank you")
            exit()
        else:
            goto(3)
    elif line == 4:
        if AGEDAY >=0:
            AGEDAY=D1-DATEOFBIRTHDAY
            goto(5)
        else:
            NEWMONTH=M1-DATEOFBIRTHMONTH-1
            NEWAGE=Y1-DATEOFBIRTHYEAR-1
            goto(6)
    elif line == 5:
        if AGEMONTH >=0:
            AGEMONTH=M1-DATEOFBIRTHMONTH
            goto(6)
        else:
            NEWAGE=Y1-DATEOFBIRTHYEAR-1
            goto(7)
    elif line == 6:
        AGEYEAR=Y1-DATEOFBIRTHYEAR
        if AGEYEAR > AGE:
            print("Sorry your date of birth is wrong or your age")
            goto(3)
        elif AGEYEAR == AGE:
            goto(8)
        else:
            print("Sorry but you are younger than what your age says, please input correct age!")
            goto(3)
    elif line == 7:
        if NEWAGE > AGE:
            print("Sorry your date of birth is wrong or your age")
            goto(3)
        elif NEWAGE == AGE:
            goto(8)
        else:
            print("Sorry but you are younger than what your age says, please input correct age!")
            goto(3)
    elif line == 8:
        NEWAGE=Y1-DATEOFBIRTHYEAR-1
        if NEWAGE < 16:
            parents=input("Have your parents or guardian already filled in this form (yes or no)? ")
            Uparents=parents.upper()
            if Uparents == 'YES':
                print("Okay, lets carry on")
                time.sleep(2)
                goto(9)
            elif Uparents == 'NO':
                print("Okay, please let your parents or guardian fill in first.")
                goto(3)
        else:
            goto(9)
            
    elif line == 9:
        WEIGHTOFBAGS=int(input("How heavey are your onboard bag's (Please put in the exact weight of each)? "))
        PRICEOFBAGS=WEIGHTOFBAGS*6
        TOTALCOSTOFBAGS=PRICEOFBAGS*NUMBEROFBAGS
        print("This is the total price £", TOTALCOSTOFBAGS,)
        PRICE=input("Would you like to continue? ")
        UPRICE=PRICE.upper()
        if UPRICE == 'NO':
            print("Okay, you are not able to board the flight. Goodbye")
            exit()
        elif UPRICE == 'YES':
            HANDPRICE=input("Do you have cabin luggage (Yes or No)? ")
            UHANDPRICE=HANDPRICE.upper()
            if UHANDPRICE == 'NO':
                print("Okay")
            elif UHANDPRICE == 'YES':
                SIZE=input("Does your luggage meet the requirement size of 16X12X6 inches (yes or no)? ")
                USIZE=SIZE.upper()
                if USIZE == 'YES':
                    print("Thank you")
                    goto(10)
                elif USIZE == 'NO':
                    print("If you still take the flight then you must pay a fine of £80")
                    bag=input("Do you still want to continue (Yes or No)? ")
                    Ubag=bag.upper()
                    if Ubag == 'NO':
                        print("Sorry but you are unable to board")
                        exit()
                    elif Ubag == 'YES':
                        FEE=80
                        goto(10)
    elif line == 10:
        WEAPON=input("Do you have any illegal substances or weapons (yes or no)? ")
        UWEAPON=WEAPON.upper()
        if UWEAPON == 'NO':
            print("Thank you")
            goto(11)
        elif UWEAPON == 'YES':
            print("Please take out weapons and place it on the side, security will check wether you are allowed these on the aircraft (this will take 30 seconds).")
            time.sleep(30)
            goto(11)
    elif line == 11:
        print("Currently you are flying from BRNO, CZECH")
        print("---------------------------------------------------------------")
        print("You are able to fly to these 5 locations (total price may vary)")
        print("London Stansted Airport, United Kindom (STN)(34.27)")#745
        print("Milan, Bergamo, Italy (BGY)(£18.63)")#405 miles
        print("Lamezia Terme, Italy (SUF)(£32.52)")#707
        print("Preveze/Lefkada, Greece (PVK)(£33.76)")#734
        print("Antalya, Turkey (AYT)(£50.69)")#1102miles
        print("---------------------------------------------------------------")
        print("Please use the three letters to pick your destination.")
        DES=input("Where would you like to go? ")
        UDES=DES.upper()
        if UDES == 'STN':
            print("1")
            break
        elif UDES == 'BGY':
            print("2")
            break
        elif UDES == 'SUF':
            print("3")
            break
        elif UDES == 'PVK':
            print("4")
            break
        elif UDES == 'AYT':
            print("5")
            break
                        
                        



    
        





            
