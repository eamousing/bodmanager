import tkinter as tk
from tkinter import ttk
from bod_import import BODImporter

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        def changeText():
            text = BODImporter().captureBOD()
            bod_info.delete(1.0,"end")
            bod_info.insert(tk.END, text)

        # Create the root window
        self.title('BOD Manager')
        # self.geometry('680x200')
        self.style = ttk.Style(self)

        # Set theme
        self.style.theme_use(themename='alt')

        # Create import BOD button
        btn = ttk.Button(self, text='Import current BOD', command= changeText) #   lambda:BODImporter().captureBOD)
        btn.grid(column=0, row=1, padx=10, pady=10,  sticky='w')

        # Create new database button
        dbBtn = ttk.Button(self, text='Create new database')
        dbBtn.grid(row=0, padx=10, pady=10, sticky="e")

        # Create text widget to hold BOD info
        bod_info = tk.Text(self, height = 1, width = 80)
        bod_info.grid(column=1, row=1, padx=10, pady=10, sticky='w')
        bod_info.insert(tk.END, "")

        # Create file Menu
        menu_bar = tk.Menu(self)
        self.config(menu = menu_bar)
        file_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label = "New database")




# if __name__ == "__main__":
#     # bodImporter = BODImporter()
#     gui = GUI()
#     gui.mainloop()