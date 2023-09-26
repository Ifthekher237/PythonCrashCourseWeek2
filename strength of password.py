#fact() finds the factorial
def fact(n):
    if n!= 0:
        result=n*fact(n-1)
    else:
        result=1
    return result




uppercase=input("Did you use any uppercase alphabet(Y/N)?")                                              #asking user ,did he/she used any upper case character is his/her password

if uppercase=="Y" or uppercase=="y":
    alphabet_uppercase=26
else:
    alphabet_uppercase = 0

lowercase=input("Did you use any lowercase character(Y/N)?")                                               #asking user ,did he/she used any lower case character is his/her password
if lowercase=="Y" or lowercase=="y":
    alphabet_lowercase=26
else:
    alphabet_lowercase = 0

number=input("Did you use any number(Y/N)?")                                                     #asking user ,did he/she used any number is his/her password
if number=="Y" or number=="y":
    total_number=10
else:
    total_number = 0

specialcharacter=input("Did you use any special character(Y/N)?")                              #asking user ,did he/she used any special character is his/her password
if specialcharacter=="Y" or specialcharacter=="y":
    total_special_character=33
else:
    total_special_character = 0

password_length=input("length of your password:")                              #take lenght of password from user
password_length=int(password_length)


totalcharacter = alphabet_uppercase + alphabet_lowercase + total_number + total_special_character


if password_length<0:
    print("How come your password length is a negative number??")
elif password_length==0:
    print("How come your password length is a zero??")

else:

    if totalcharacter > 0:
        total_permutation=fact(totalcharacter)/fact(totalcharacter-password_length)         #calling the fact() function to calculate factorial
        print("The hacker needs to try " + str(total_permutation) + " times to hack your password")
    else:
        print("May be you are joking with me!!")


