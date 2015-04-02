from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Get file")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)

        self.button = Button(self, text="Browse", command=self.get_file, width=10)
        self.button.grid(row=1, column=0, sticky=W)
        self.button1 = Button(self, text="", command=self.get_file, width=10)

    def get_file(self):
        fname = askopenfilename(filetypes=(("Template files", "*.tplate"),
                                           ("Text files", "*.txt;*.htm"),
                                           ("All files", "*.*") ))
        return fname


if __name__ == "__main__":
    MyFrame().mainloop()
