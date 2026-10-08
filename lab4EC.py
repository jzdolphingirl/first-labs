import random

Player1 = input("Enter player 1 name: ")
Player2 = input("Enter player 2 name: ")
Total1 = 0
Total2 = 0
turn1 = True
while True:
    Score1 = 0
    Score2 = 0
    while turn1:
        roll = input(f"{Player1}, type r to roll! ")
        if roll == "r":
            num1 = random.randint(1,6)
            num2 = random.randint(1,6)
            print(f"You rolled a {num1} and a {num2}")
            if num1 == 1 and num2 == 1:
                Score1 += 25
                print(f"Your round score is {Score1}, and your total score is {Total1 + Score1}")
                if Total1 + Score1 >= 100:
                    break
            elif num1 == num2:
                Score1+= 4*num1
                print(f"Your round score is {Score1}, and your total score is {Total1 + Score1}")
                if Total1 + Score1 >= 100:
                    break
            elif num1 == 1 or num2 == 1:
                turn1 = False
                Score1 = 0
                print("Your turn is over! Your round score is 0")
                break
            else:
                Score1 += num1+num2
                print(f"Your current score is {Score1}, and your total score is {Total1 + Score1}")
                if Total1 + Score1 >= 100:
                    break
            answer = input("Would you like to roll again (type 'r') or end your turn (type 'q')? ")
            if answer == "r":
                turn1 = True
            else:
                turn1 = False
    Total1 += Score1
    print (f"{Player1} now has {Total1} total points")
    if Total1>= 100:
        print(f"{Player1} wins! Congrats!")
        break
        
    while not turn1:
        roll = input(f"{Player2}, type r to roll! ")
        if roll == "r":
            num1 = random.randint(1,6)
            num2 = random.randint(1,6)
            print(f"You rolled a {num1} and a {num2}")
            if num1 == 1 and num2 == 1:
                Score2 += 25
                print(f"Your round score is {Score2}, and your total score is {Total2 + Score2}")
                if Total2 + Score2 >= 100:
                    break
            elif num1 == num2:
                Score2+= 4*num1
                print(f"Your round score is {Score2}, and your total score is {Total2 + Score2}")
                if Total2 + Score2 >= 100:
                    break
            elif num1 == 1 or num2 == 1:
                turn1 = True
                Score2 = 0
                print("Your turn is over! Your round score is 0")
                break
            else:
                Score2 += num1+num2
                if Total2 + Score2 >= 100:
                    break
                print(f"Your current score is {Score2}, and your total score is {Total2 + Score2}")
            answer = input("Would you like to roll again (type 'r') or end your turn (type 'q')? ")
            if answer == "r":
                turn1 = False
            else:
                turn1 = True
    Total2 += Score2
    print (f"{Player2} now has {Total2} total points")
    if Total2>= 100:
        print(f"{Player2} wins! Congrats!")
        break


