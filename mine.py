import random
import os
 
# Printing the Minesweeper Layout
def print_mines_layout():
 
    global mine_values
    global n
 
    print()
    print("\t\t\tMINESWEEPER\n")
    
    #top numbers
    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)   
 
    for r in range(n):
        st = "     "
        #top line
        if r == 0:
            for col in range(n):
                st = st + "______" 
            print(st)

        #first set of bars
        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")

        #edge number + mine value; render all zero representations as blank
        st = "  " + str(r + 1) + "  "
        for col in range(n):
            value = mine_values[r][col]
            shown = " " if str(value).strip() == "0" else str(value)
            st = st + "|  " + shown + "  "
        print(st + "|") 

        #side + bottom
        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')
 
    print()
  
def set_mines(first_r, first_col):
    global numbers
    global mines_no
    global n

    # Clear any previous board state before placing mines
    numbers = [[0 for _ in range(n)] for _ in range(n)]

    # Protect the first clicked cell and the full 3x3 area around it
    blocked = {
        (r, c)
        for r in range(n)
        for c in range(n)
        if abs(r - first_r) <= 1 and abs(c - first_col) <= 1
    }

    available = [
        (r, c)
        for r in range(n)
        for c in range(n)
        if (r, c) not in blocked
    ]

    if mines_no > len(available):
        raise ValueError("Too many mines for the board and safe opening area.")

    for r, c in random.sample(available, mines_no):
        numbers[r][c] = -1
 
# Function for setting up the other grid values
def set_values():
 
    global numbers
    global n
 
    # Loop for counting each cell value
    for r in range(n):
        for col in range(n):
 
            # Skip, if it contains a mine
            if numbers[r][col] == -1:
                continue
 
            # Check up  
            if r > 0 and numbers[r-1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check down    
            if r < n-1  and numbers[r+1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check left
            if col > 0 and numbers[r][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check right
            if col < n-1 and numbers[r][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check top-left    
            if r > 0 and col > 0 and numbers[r-1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check top-right
            if r > 0 and col < n-1 and numbers[r-1][col+1]== -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check below-left  
            if r < n-1 and col > 0 and numbers[r+1][col-1]== -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check below-right
            if r < n-1 and col < n-1 and numbers[r+1][col+1]==-1:
                numbers[r][col] = numbers[r][col] + 1
 
# Recursive function to display all zero-valued neighbours  
def neighbours(r, col):
     
    global mine_values
    global numbers
    global vis

    # If the cell already not visited
    if [r,col] not in vis:
 
        # Mark the cell visited
        vis.append([r,col])
 
        # If the cell is zero-valued
        if numbers[r][col] == 0:
 
            # Keep zero numeric internally; print_mines_layout renders it blank
            mine_values[r][col] = 0
 
            # Recursive calls for the neighbouring cells
            if r > 0:
                neighbours(r-1, col)
            if r < n-1:
                neighbours(r+1, col)
            if col > 0:
                neighbours(r, col-1)
            if col < n-1:
                neighbours(r, col+1)    
            if r > 0 and col > 0:
                neighbours(r-1, col-1)
            if r > 0 and col < n-1:
                neighbours(r-1, col+1)
            if r < n-1 and col > 0:
                neighbours(r+1, col-1)
            if r < n-1 and col < n-1:
                neighbours(r+1, col+1)  
 
        # If the cell is not zero-valued            
        if numbers[r][col] != 0:
            mine_values[r][col] = numbers[r][col]
 
# Function for clearing the terminal
def clear():
    os.system("clear")      
 
# Function to display the instructions
def instructions():
    print("Instructions:")
    print("1. Enter row and column number to select a cell, Example \"2 3\"")
    print("2. In order to flag a mine, enter F after row and column numbers, Example \"2 3 F\"")
 
# Function to check for completion of the game
def check_over():
    global mine_values
    global n
    global mines_no
 
    # Count of all numbered values
    count = 0
 
    # Loop for checking each cell in the grid
    for r in range(n):
        for col in range(n):
 
            # If cell not empty or flagged
            if mine_values[r][col] != ' ' and mine_values[r][col] != 'F':
                count = count + 1
     
    # Count comparison          
    if count == n * n - mines_no:
        return True
    else:
        return False
 
# Display all the mine locations                    
def show_mines():
    global mine_values
    global numbers
    global n
 
    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:
                mine_values[r][col] = 'M'
 
 
if __name__ == "__main__":
 
    # Size of grid
    n = 8
    # Number of mines
    mines_no = 8
 
    # The actual values of the grid
    numbers = [[0 for y in range(n)] for x in range(n)] 
    # The apparent values of the grid
    mine_values = [[' ' for y in range(n)] for x in range(n)]
    # The positions that have been flagged
    flags = []
 
    # Do not place mines yet; wait until the first cell is opened.
    first_move = True

    # Display the instructions
    instructions()

    #   Variable for maintaining Game Loop
    over = False
     
    # The GAME LOOP 
    while not over:
        print_mines_layout()
 
        # Input from the user
        inp = input("Enter row number followed by space and column number = ").split()
         
        # Standard input
        if len(inp) == 2:
 
            # Try block to handle errant input
            try: 
                val = list(map(int, inp))
            except ValueError:
                clear()
                print("Wrong input!")
                instructions()
                continue
 
        elif len(inp) == 3:
            if inp[2] != 'F' and inp[2] != 'f':
                clear()
                print("Wrong Input!")
                instructions()
                continue

            try:
                val = list(map(int, inp[:2]))
            except ValueError:
                clear()
                print("Wrong input!")
                instructions()
                continue

            if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
                clear()
                print("Wrong input!")
                instructions()
                continue

            r = val[0]-1
            col = val[1]-1

            # Do not place mines when flagging
            if [r, col] in flags:
                clear()
                print("Flag already set")
                continue

            if mine_values[r][col] != ' ':
                clear()
                print("Value already known")
                continue

            if len(flags) < mines_no:
                clear()
                print("Flag set")
                flags.append([r, col])
                mine_values[r][col] = 'F'
                continue
            else:
                clear()
                print("Flags finished")
                continue    
 
        else: 
            clear()
            print("Wrong input!")   
            instructions()
            continue
             
 
        # Sanity checks
        if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
            clear()
            print("Wrong Input!")
            instructions()
            continue
             
        # Get row and column number
        r = val[0]-1
        col = val[1]-1

        if first_move:
            set_mines(r, col)
            set_values()
            first_move = False

        # Unflag the cell if already flagged
        if [r, col] in flags:
            flags.remove([r, col])

        # If landing on a mine --- GAME OVER
        if numbers[r][col] == -1:
            mine_values[r][col] = 'M'
            show_mines()
            print_mines_layout()
            print("Landed on a mine. GAME OVER!!!!!")
            over = True
            continue

        elif numbers[r][col] == 0:
            vis = []
            mine_values[r][col] = 0
            neighbours(r, col)

        else:
            mine_values[r][col] = numbers[r][col]
 
        # Check for game completion 
        if(check_over()):
            show_mines()
            print_mines_layout()
            print("Congratulations!!! YOU WIN")
            over = True
            continue
    clear() 