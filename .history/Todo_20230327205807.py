from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root 
    
 
def main():
     root = Tk()
     ui = todo(root)
     root.mainloop()  
     
if __name__ == "__main__" :
    main()
          