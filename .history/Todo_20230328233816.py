from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('Kiki\'s Ta\'doo\'s') 
        self.root.geometry('575x400+200+100')
        
        self.lbl = Label(self.root, text= 'Kiki\'s Ta\'doo\'s', font= 'calabri, 30 bold', fg= 'red', width=5,bd=10, bg='black')
        self.lbl.pack(side= 'top', fill= BOTH)
        
        
        self.lbl2 = Label(self.root, text= 'Add Ta\'doo', font= 'calabri, 25 bold', fg= 'black', width=15,bd=10, bg='red')
        self.lbl2.place(x)
        
                               
def main():
     root = Tk()
     ui = todo(root)
     root.mainloop()  
     
if __name__ == "__main__" :
    main()
          