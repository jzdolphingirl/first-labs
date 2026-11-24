import tkinter as tk

window = tk.Tk()
window.title("Draft")
canvas = tk.Canvas(window, width = 1500, height = 840, bg = "white")
canvas.pack()

canvas.create_rectangle(20,20,820,820, fill="orange", outline="black", width = 2) #board
canvas.create_rectangle(840,20,1480,150, fill="purple", outline="black", width = 2) #timer
canvas.create_rectangle(840,170,1480,820, fill="teal", outline="black", width = 2) #scores

boardt = canvas.create_text(410, 410, text="board", font=("Ariel", 30, "bold"), fill="black")
boardt = canvas.create_text(1160, 85, text="timer", font=("Ariel", 30, "bold"), fill="black")
boardt = canvas.create_text(1160, 495, text="scores", font=("Ariel", 30, "bold"), fill="black")



#label = tk.Label(window, text="My name is Jiening") #just text at the top
#label.pack() #places the label inside the window.

#button = tk.Button(window, text="Stop", width=100, command=window.destroy) #button that closes the program when clicked
#button.pack()

#tk.Label(window, text = "First Name").grid(row=0, column=0) #single line inputs
#tk.Label(window, text = "Last Name").grid(row=1, column=0)

#entry1 = tk.Entry(window)
#entry2 = tk.Entry(window)

#entry1.grid(row=0, column=1)
#entry2.grid(row=1, column = 1)

window.mainloop()