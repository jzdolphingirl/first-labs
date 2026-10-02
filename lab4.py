# while (True):
#     c = int(input("Enter a number (0 to exit): "))
#     if c == 0:
#         break
#     print(f"Multiplication table for {c}")  

#     for i in range(c): #this is the for loop in python
#        product = i * c
#        print(f"{i} x {c} = {product}") 

while(True):
    c = int(input("Enter a non-negative number (0 to exit): "))
    if(c<0):
        print("Error, number cannot be negative")
    elif(c == 0):
        break
    factor = 2
    factors = []
    num = c
    while num>=2:
        if num % factor == 0:
            factors.append(factor)
            num = num / factor
        else:
            factor +=1
    print(f"The prime factors of {c} are:", end=" ")
    print(*factors, sep=", ")