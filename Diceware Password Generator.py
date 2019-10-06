#This is a passphrase generator based on the Diceware method of passphrase generation.

#Import random module and the Diceware Word list dictionary
import random
from DiceDictionary import DiceDict as DD
from DiceDictionary import SymbolList as SL
print("This is a passphrase generator based on the Diceware method of passphrase generation, ")
      #"\nYou will be asked how long you want your passphrase, and after generation, "
      #"\nYou will be asked if you want to add symbols, add numbers, and/or save your password to a text file.")

#Ask user how long they want the passphrase to be
LengthValid = False
while LengthValid == False:

    Length = (input("Please enter how many words long you would like your passphrase \n(between 5-10, Recommended:7):"))

    try:
        if int(Length) >= 5 and int(Length) <= 10:
            LengthValid = True
        else:
            print("That is not a valid number.")
    except ValueError:
        print("That is not a number.")
        continue


#Roll 5 dice, add their values to a list (Passwords)
Passwords = []
P = 1
while P <= int(Length): #Stop when there are X words (Defined by user) from the dictionary in the passphrase
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
while pp < int(Length):
    Passphrase += str(Passwords[pp])
    pp += 1
print(Passphrase.capitalize())

#Check if user wants to add a random symbol/number/caps etc. into the passphrase, or if they want to save it to a text file.
"""inputValid = False
while inputValid == False:
        Symbol = input("\nHere is your super strong passphrase. If you want to make it extra secure, \n"
                       "you can replace a random character with a random symbol \n"
                       "(You may wish to skip this if your generatd password already has a symbol). (Y/N): ").upper()

        if str(Symbol) == "Y":
           Range = len(Passphrase)
           Char = random.randint(0:Range)
           Sym = random.choice(SL)
           Passphrase[Char] = Sym
           inputValid = True
        elif str(Symbol) == "N":
            inputValid = True
        else:
            print("That is not a valid answer (1)")

print(Passphrase.capitalize())
inputValid = False
while inputValid == False:
    try:
        number = input("\nWould you like to replace a random character with a random number? \n"
                       "(You may wish to skip this if your generatd password already has a number). (Y/N): ").upper()

        if str(number) == "Y":
           Range = len(Passphrase)
           validNum == False
           while validNum == False:
               Char2 = random.randint(0, Range)
               if Char2 != Char:
                   break
               else:
                   continue
           Sym = random.choice(SL)
           Passphrase[char2] = Sym
           inputValid = True
        elif str(number) == "N":
            inputValid = True
        else:
            print("That is not a valid answer")
    except:
            print("That is not a valid answer.")
Print = input("Would you like to save your ")"""