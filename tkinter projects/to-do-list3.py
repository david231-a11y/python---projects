from tkinter import *


class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry('650x410+300+150')

        self.label =Label(self.root,text="To-Do-List-App",font='ariel 25, bold',width=10,bd=5,bg='red',fg='black')
        self.label.pack(side= 'top',fill= BOTH)




def main() :
    root = Tk()
    ui = todo(root)
    root.mainloop()  

if __name__ == "__main__":
    main()  