#Guess Number game
import random

print("Whats your name")
name = input()
print("Well," , name , "i am thinking of a number between 1 and 20.", sep=" ")
print("take a guess")
number = random.randint(1,21)
count = 0
isFoundNumber = 0
try:
    while count < 5:
        userNumber = input()
        if int(userNumber) > number:
            print("too high")
        elif int(userNumber) < number:
            print("too low")
        else:
            print("gotcha","you got in",str(count),"turn", sep=" ")
            isFoundNumber += 1
            break
        count += 1
    if isFoundNumber < 1 :
        print("sorry", "you wouldnt get in", str(count)+"turn", sep = " ")       
        
except:
    print("Error Occured")
