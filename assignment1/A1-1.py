# Govinda Baweja
# Assignment 1
# Date: 04-26-2019


# Raw Input
x = raw_input("Please Enter a Number and not a string\n")
print ("The value of x is: "),x
print ("The data type is: "),type(x)

#Raw Input with type conversion to integer
y = int(raw_input("\nPlease Enter a Number\n"))
print ("The value of y is: "),y
print ("The data type is: "),type(y)

#Raw Input with type conversion to string
r = str(raw_input("\nPlease Enter STRING\n"))
print ("The value of r is: "),r
print ("The data type is: "),type(r)

#Raw Input with eval
z = eval(raw_input("\nPlease Enter a Number or a Float\n"))
print ("The value of z is: "),z
print ("The data type is: "),type(z)


#Input function with Python2 is same as eval(raw_input())
p = input("\nPlease Enter a Number or a Float\n")
print ("The value of p is: "),p
print ("The data type is: "),type(p)


#Input function with Python3 will work same as python2 but the difference is in python3 it is a class and not a function
q = input("\nPlease Enter a Number or a Float\n")
print ("The value of q is: "),q
print ("The data type is: "),type(q)
