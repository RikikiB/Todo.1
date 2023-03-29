from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('Kiki\'s-Tadoo\'s') 
        self.root.geometry('575x400+200+100')
        
        self.label = Label(self.root, text= 'Kiki\'s Tadoo\'s', font= 'calabri, 20 bold', fg= 'red', width=15,bd=10, bg='black')
        self.label.pack(side= 'top', fill= BOTH)
        
        
                               
def main():
     root = Tk()
     ui = todo(root)
     root.mainloop()  
     
if __name__ == "__main__" :
    main()
          