"""
#this program shows whether the entered year is a leap year
year=input("input a year:")
year=int(year)
def leap_year(year):
  if year % 4==0:
    print("leaf year")
  else:
    print("not leap year")
leap_year(year)
"""
"""
#this program shows whether the given values can make a triangle
a,b,c=input("Input three values without any space(example::if a=1,b=2,c=10 ,then input 1210)")
a=int(a)
b=int(b)
c=int(c)
def triangle(a,b,c):
  if a+b>c and a+c>c and b+c>a :
    print("you have entered right number!")
    print("you can make a triangel now")
  else:
    print("Ooops! you must recheck your entered numbers")
triangle(a,b,c)
"""
"""
#this program finds the factorial of a given number.

def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
result=fact(5)
print(result)
"""
"""
#this prigram is an example of recursion.
def tri_recursion(k):
  print("factorial has been called with n = " + str(k))
  if(k > 0):
    print("now2")
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    print("now")
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
"""


"""
#this program demonstrates how to find ceiling of a given float number.
import math
print(math.ceil(2.8))
"""





j=int(input("enter a number greater than 1"))
for i in range(2,j):
    if j%i==0:
        continue
    else:
        print("prime")





















