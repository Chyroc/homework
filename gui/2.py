import tkinter as tk


class OKCannel(object):
    def show_ok(self, ):
        self.my_string_var.set("OK button is clicked")

    def show_cannel(self):
        self.my_string_var.set("Cancel button is clicked")

    def run(self):
        self.root = tk.Tk()
        self.root.title('yyy')

        self.my_string_var = tk.StringVar(value="")
        my_label = tk.Label(self.root, textvariable=self.my_string_var)
        my_label.pack()

        tk.Button(self.root, text='OK', command=self.show_ok, fg='red').pack(side=tk.TOP)
        tk.Button(self.root, text='Cannel', command=self.show_cannel, bg='yellow').pack(side=tk.BOTTOM)
        tk.mainloop()


if __name__ == '__main__':
    OKCannel().run()
