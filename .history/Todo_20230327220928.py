from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('Kikis-Tadoo') 
        self.root.geometry('400x300+200+100')
        
        self.label = Label(self.root, text= 'Kikis Tadoo', font= 'calabri, 20 bold', width= 15,bd=10 bg='blac')
        
                               
def main():
     root = Tk()
     ui = todo(root)
     root.mainloop()  
     
if __name__ == "__main__" :
    main()
          