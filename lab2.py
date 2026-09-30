# token = input("Input a string: ")
# length = int(input(f"Input a number between 1 and {round(len(token)/2)}: "))
# first = token[:length]
# middle = token[length: len(token)-length]
# end = token[len(token)-length:]
# print(f"{token} with the first {length} and last {length} characters swapped is: {end}{middle}{first}")

fullName = input("Enter a name in (first, middle, last) format: ")

firstSpace = fullName.index(" ")
firstName = fullName[:firstSpace]
secondSpace = fullName.index(" ", firstSpace + 1)
middleName = fullName[firstSpace + 1:secondSpace]
lastName = fullName[secondSpace + 1:]

firstInitial = firstName[:1]
midInitial = middleName[:1]
lastInitial = lastName[:1]

print("Initials: " + firstInitial + midInitial + lastInitial)
print("Rearranged Name: " + lastName + ", " + firstName + " " + midInitial + ".")


print(firstName)
print(middleName)
print(lastName)

