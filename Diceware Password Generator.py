#This is a password generator based on the Diceware method of passphrase generation

#Import random module and the Diceware Word list dictionary
import random
from DiceDictionary import DiceDict as DD


#Ask user how strong they want the pasword to be
LengthValid = False

while LengthValid == False:

    Length = int(input("Please enter how many words long you would like your passphrase \n(between 5-10, Recommended:7):"))

    try:
        if Length >= 5 and Length <= 10:
            LengthValid = True
        else:
            print("That is not a valid number.")
    except:
        print("That is not a number.")



#Roll 5 dice, add their values to a list (Passwords)
Passwords = []
P = 1
while P <= Length: #Stop when there are X words (Defined by user) from the dictionary in the passphrase
    TotalRoll = []

    i = 1
    TR = 0
    TotalRollConcat = ""
    while i <= 5:
        Diceroll = random.randint(1,6)
        TotalRoll.append(Diceroll)
        i += 1


    #Concatenate the Dice rolls
    while TR != 5:
        TotalRollConcat += str(TotalRoll[TR])
        TR += 1




    #Grab the value with our generated key from the dictionary

    Word = DD[int(TotalRollConcat)]
    Passwords.append(Word)
    P += 1

#Concatenate the words in the password list
Passphrase = ""
pp = 0
while pp < Length:
    Passphrase += str(Passwords[pp])
    pp += 1
print(Passphrase)

#check if user wants to add a random symbol/number/caps etc. into the password, or if they want to save it to a text file.
"""try:
    Symbol = input("\n Here is your super strong password. If you want to make it extra secure, \nyou can replace a random character with a random symbol. (Y/N): ")

    if Symbol == "Y":
       Range = len(Passphrase)
       Passphrase.replace()

except:
        


Print = input("Would you like to save your ")"""