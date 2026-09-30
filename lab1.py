import math

# print("hello, world")
# print("\nmy name is jiening")

# age=17
# price=19.99
# first_name = "Jiening"
# good = True

# print("my name is " + first_name + " and I am " + str(age) + " years old. The price of my shirt was $" + str(price) + ".")
# print(f"my name is {first_name} and I am {age} years old. The price of my shirt was ${price}.")

# this is a comment

#Differences between Java and Python
#Variables: Python does it automatically while in Java you need to specify what type of variable it is
#Print: has to be all strings, can either convert to string using str() 
    #or use an f string + curly braces which automatically converts into text

# x=10
# y=8
# sum = x + y
# print(sum) #no need to format cause no text strings

# division = 11/2

# print(f"{division}") #this one prints the decimal
# print(int(division)) #this one truncates the decimal into an int
# print(int(round(division))) #this one rounds the decimal to the nearest int

# sum_value = 10.25 * 11.99
# print(sum_value)

# if len(str(sum_value)) > 3: #convert to string, then use length. also if statement format???
#     print(division)

# print(len(str(division)))

# first_num = int(input("enter your first number: ")) #accepts input, then casts int because input is a string
# second_num = int(input("enter your second number: "))
# third_num = int(input("enter your third number: "))
# fourth_num = int(input("enter your fourth number: "))
# fourth_num = int(input("enter your fifth number: "))

# result1 = first_num + second_num
# result2 = result1 * third_num
# result3 = result2 - fourth_num
# print(f"{first_num} + {second_num} = {result1}")
# print(f"{result1} * {third_num} = {result2}")
# print(f"{result2} - {fourth_num} = {result3}")
# print(f"{result3} / {fourth_num} = {round(result3/fourth_num, 2)}")

# radius = float(input("enter radius length: "))
# print(f"Diameter: {radius * 2}")
# print(f"Circumference: {round(2 * radius * math.pi, 2)}")
# print(f"Surface Area: {round(4 * radius ** 2 * math.pi, 2)}")
# print(f"Volume: {round(4 / 3 * math.pi * radius ** 3, 2)}") # ** is the easiest way to do powers

while True:
    num = int(input("enter an integer with 4 digits:"))
    if abs(num)>9999 or abs(num)<1000:
        print("TRY AGAIN. ")
    else:
        break
is_negative = num<0

thousands = abs(num)//1000*1000
hundreds = abs(num)%1000//100*100
tens = abs(num)%100//10*10
ones = abs(num)%10

if is_negative:
    print(f"{num} = -{thousands} - {hundreds} - {tens} - {ones}")
else:
    print(f"{num} = {thousands} + {hundreds} + {tens} + {ones}")

# A = int(input("Enter A: "))
# B = int(input("Enter B: "))
# C = int(input("Enter C: "))
# if round(C / B, 2) > 0:
#     print(f"Slope-intercept Equation: y = {round(-1 * A / B, 2)}x + {round(C / B, 2)}")
# else:
#     print(f"Slope-intercept Equation: y = {round(-1 * A / B, 2)}x - {abs(round(C / B, 2))}")