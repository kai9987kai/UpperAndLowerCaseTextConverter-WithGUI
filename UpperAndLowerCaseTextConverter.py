import tkinter as tk

class YourGUI(tk.Tk):
    def __init__(self):
        # inherit tkinter's window methods
        tk.Tk.__init__(self)

        tk.Label(self, text="ENTER TEXT:")\
            .grid(row=0, column=0)
        self.input = tk.Entry(self)
        self.input.grid(row=0, column=1)

        tk.Label(self, text="CONVERTED TO LOWER CASE:")\
            .grid(row=1, column=0)
        self.result_lower = tk.Entry(self)
        self.result_lower.grid(row=1, column=1)

        tk.Label(self, text="CONVERTED TO UPPER CASE:")\
            .grid(row=2, column=0)
        self.result_upper = tk.Entry(self)
        self.result_upper.grid(row=2, column=1)

        tk.Button(self, text="convert", command=self.do_conversion)\
            .grid(row=3, column=0, columnspan=2)



    def do_conversion(self):
        self.result_lower.delete(0, tk.END)
        self.result_upper.delete(0, tk.END)

        phrase = self.input.get()
        self.result_lower.insert(0, phrase.lower())
        self.result_upper.insert(0, phrase.upper())

if __name__ == '__main__':
    your_gui = YourGUI()
    your_gui.mainloop()
