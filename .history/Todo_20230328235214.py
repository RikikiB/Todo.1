from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('Kiki\'s Ta\'doo\'s') 
        self.root.geometry('600x400+200+100')
        
        self.lbl = Label(self.root, text= 'Kiki\'s Ta\'doo\'s', font= 'calabri, 30 bold', fg= 'red', width=15,bd=10, bg='black')
        self.lbl.pack(side= 'top', fill= BOTH)
        
        
        self.lbl2 = Label(self.root, text= 'Add Ta\'doo', font= 'calabri, 30 bold', fg= 'black', width=10,bd=5, bg='red')
        self.lbl2.place(x=-9, y=84)
        
        
        self.lbl3 = Label(self.root, text= 'Ta\'doo\'s', font= 'calabri, 30 bold', fg= 'red', width=10,bd=5, bg='black')
        self.lbl3.place(x=-9, y=130)
        
        
        self.main_txt = Listbox(self.root, width= 30, height= 10, bd=8, font= 'calabri, 20 bold')
        self.main_txt.place(x=-9, y=180)
                               
def main():
     root = Tk()
     ui = todo(root)
     root.mainloop()  
     
if __name__ == "__main__" :
    main()
          