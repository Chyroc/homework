import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title('yyy')
    tk.Label(root,text='Welcome to Python Tkinter').pack()
    tk.Button(root, text='Click Me').pack(side=tk.BOTTOM)
    tk.mainloop()
