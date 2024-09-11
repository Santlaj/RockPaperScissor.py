'''
this
is a
multi
line
comment
'''
from pickle import STRING

#escape sequence(\n)
#escape sequene is used for breaking the line of string.we don't have to give space after writing \n
print("Hey i'm a good boy \nand my friends are also good")

print("Hey i'm a \"good boy \"\nand my friends are also good")       #\" is a double code escape sequence character

#Separator
print("Hey",6,7, sep="~")
print(6,7,8,9,10,11,12,13,14,15,sep="  ",end="009 ")
print("hello")

#VARIABLES AND DATA TYPE
a=1234.00                                     # a is variable and 1234 is data stored in it
print(a)
print("Type of a is:",type(a))                # this will show the type data type stored in it
b="Harry"
print(b)
print("Type of a is:",type(b))

#CALCULATIONS
print(15/7)
print(15//7) #floor division
print(15%7)  #remainder

 #TYPECASTING       (CONVERSION OF ONE DATA TYPE  INTO OTHER DATA TYPE IS KNOWN AS TYPE CASTING)
#Explicit type conversion
c= 2
d= 7
print(type(c+d))
print(type(float(c+d))) #this is called type casting

#Implicit type conversion means type will automatically converted by python
c=5
d=9.9
print(c+d)

#TAKING USER INPUTS
# a=input()
# print("My name is :",a)
# a=int(input("first number is: ",))
# b=int(input("first number is: ",))
# print(a+b)


name="SANTLAJ"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
# print(name[7])  this will give error
for character in name:
    print(character)

#STRING
name="Santlaj"
print(name.upper())
print(name.lower())
print(name[0:])
print(len(name)) #used for finding length of string
print(name[0:len(name)-2])
print(name[-4:-2])
a="sanju!!!!sanju"
print(a)
print(a.count("sanju")) #it will count how many times sanju is in a
print(a.rstrip("!")) # a.rstrip removes special characters from strings
print(a.replace("!","$"))
print(a.split(" "))
print(a.capitalize()) #first character will be chnged to upercase

str1="Welcome to the console to!!!"
print(len(str1))
print(len(str1.center(50)))
print(str1.endswith("to",4,10))

#FIND METHOD
print(str1.find("to")) #what if we have two same data and we have to find the length of second one

#INDEX METHOD
print(str1.index("sanju")) #this method will five error when it will not find the given value in variable but in find method it will give an output of -1

# print(str1.isalnum())
# print(str1.isalpha())
#print(str1.isprintable())
#print(str1.isspace())
#print(str1.istitle())
#print(str1.swapcase())



