import os
from tkinter import *
from tkinter import filedialog

class UIAPP(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()
    
    def init_ui(self):
        self.parent.title("Computer Cleaner!")
        title_one = Label(self.parent, text="Welcome to your Computer Cleaner!")
        title_one.pack(pady=1)
        subtitle_one = Label(self.parent, text="Choose the type of extension you'd like to delete:")
        subtitle_one.pack(pady=5)
        self.jpeg = IntVar()
        self.pdf = IntVar()
        self.zip = IntVar()
        self.exe = IntVar()
        Checkbutton(self.parent, text=".jpeg", variable=self.jpeg, onvalue=1, offvalue=0).pack()        
        Checkbutton(self.parent, text=".exe", variable=self.exe, onvalue=1, offvalue=0).pack()        
        Checkbutton(self.parent, text=".pdf", variable=self.pdf, onvalue=1, offvalue=0).pack()        
        Checkbutton(self.parent, text=".zip", variable=self.zip, onvalue=1, offvalue=0).pack()        

        self.choose_path_button = Button(self.parent, text="Choose a path", command=self.on_path_click)
        self.choose_path_button.pack(pady=10)
        
        self.run_button = Button(self.parent, text="Run", command=self.on_run_click, state=DISABLED)
        self.run_button.pack()

    def FileDeleter(self, dw_path, ending):
        for root, dirs, files in os.walk(dw_path):
            for file in files:
                if file.endswith(ending):
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        print(f"File deleted: {file_path}") 
                    except OSError as e:
                        print(f"Error deleting file: {file_path} - {e}")

    def choose_path(self):
        self.chosen_path = filedialog.askdirectory()
        self.check_selection()
        print(self.chosen_path)

    def on_path_click(self):
        self.choose_path()
    
    def check_selection(self):
        if hasattr(self, 'chosen_path') and (self.jpeg.get()) or (self.pdf.get()) or (self.zip.get()) or (self.exe.get()):
            self.run_button.configure(state=NORMAL)
        else:
            self.run_button.configure(state=DISABLED)

    def on_run_click(self):
        if self.jpeg.get():
            self.FileDeleter(self.chosen_path, ".jpeg")
        if self.pdf.get():
            self.FileDeleter(self.chosen_path, ".pdf")
        if self.zip.get():
            self.FileDeleter(self.chosen_path, ".zip")
        if self.exe.get():
            self.FileDeleter(self.chosen_path, ".exe")
        

if __name__ == "__main__":
    ROOT = Tk()
    ROOT.geometry("400x250")
    APP = UIAPP(parent=ROOT)
    APP.mainloop()


