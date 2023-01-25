#Write a function named only_ints that takes two parameters.
# Your function should return True if both parameters are integers, and False otherwise.

def only_ints (x,y):
    if type (x) != int or type (y) != int:
        print ("False"),
    else:
        print ("True")

#try with two numbers
x = 5
y = 9
only_ints(x,y)

#try with math on integers
x=x+1
y=y*8
only_ints(x,y)

#try with a boolean
x=True
y=5
only_ints(x,y)

#try with an integer and a float
x=8.76543
y=2
only_ints(x,y)

#try with inputting a number, which will be typed a string
x=input("Please type a number")
y=input("Please type another number")
only_ints(x,y)

#try with inputting a number and changing it to an integer
x=int(input("Please type a number"))
y=int(input("Please type another number"))
only_ints(x,y)

