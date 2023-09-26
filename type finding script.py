#the motive of this script is to determine the type of a user given value

import math                                                              # because of using "import math" , i can find the ceiling of given number

#this function determines the type of the given value
def get_type(value):
    number = input("Now input :")                                           #finally to take the value from the user
    if value=="1":
 #if 1 is pressed then within an if-else block the following if-else block will be interpreted
        number=float(number)                                                  #as by default , taken value is condisered as string , we have to convert the number string to actual number .That's why float() function is used
        if math.ceil(number)==number :                                        #this condition checks whether the number is float or integer
            print("\nYou have entered an INTEGER type value\n\n")
        else:
            print("\nYou have entered a FLOAT type value\n\n")
 #if 2 is pressed then the following block will be interpreted
    else:
         print("\nYou have entered a STRING\n\n")
    print("Thank you for using the script. To mail the author of the script <ifthekher.du@gmail.com>")


print('                              |\"""""|___ ')                             #These lines are
print('                              | \      | ')                              #just for making
print('                              |  \/    | ')                              #the script
print('                              |  /\    | ')                              #looks
print('                              |____\___| ')                              #good.

print("\n                 This script find the type of your inputted value\n")  #shows the motive of the script.
print("Usage::")                                                                #This lines
print("       For a bunch of number press 1")                                   #tell the user
print("       For a bunch of alphabet press 2\n")                               #how to use
value=input("\n Okay...so which one you are gonna input(1/2):")                 #the script.


get_type(value)                                                                   #calls the function.