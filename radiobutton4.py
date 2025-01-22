from tkinter import *

playstation = ["playstation1", "playstation2", "playstation3", "playstation4", "playstation5"]

def order():
    if x.get() == 0:
        print("You ordered a playstation1!")
    elif x.get() == 1:
        print("You ordered a playstation2!")
    elif x.get() == 2:
        print("You ordered a playstation3!")
    elif x.get() == 3:
        print("You ordered a playstation4!")
    elif x.get() == 4:
        print("You ordered a playstation5!")

window = Tk()
window.title("A cool playstation ordering app")
window.geometry("600x600")
window.config(background="orange")

x = IntVar()

# Labels for each PlayStation model
labels = [
    "Click to buy a PlayStation 1",
    "Click to buy a PlayStation 2",
    "Click to buy a PlayStation 3",
    "Click to buy a PlayStation 4",
    "Click to buy a PlayStation 5"
]

for index in range(len(playstation)):
    radio_button = Radiobutton(window, text=[index], font=('Impact', 50), variable=x, padx=35, 
                               width=575, indicatoron=0, value=index, fg="green", command=order)
    radio_button.pack()
    
    # Add a label below each radio button
    label = Label(window, text=labels[index], font=('Arial', 12), bg="orange")
    label.pack()

window.mainloop()
