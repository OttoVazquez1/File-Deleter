import os
import tkinter as tk
from tkinter import filedialog


class UIAPP(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()
    
    def init_ui(self):
        self.parent.title("Computer Cleaner!")
        choose_path_button = tk.Button(self.parent, text="Choose a path", command=self.on_path_click)
        choose_path_button.pack()
        btn = tk.Button(self.parent, text="Carlitos", command=print(path))
        btn.pack()



    def FileDeleter(dw_path, ending):
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
        root = tk.Tk()
        root.withdraw()
        path = tk.filedialog.askdirectory()
        root.destroy()
        return path

    def on_path_click(self):
    
        chosen_path = self.choose_path()
        path = chosen_path
        return chosen_path

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("300x100")
    APP = UIAPP(parent=ROOT)
    APP.mainloop()