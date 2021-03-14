import tkinter as tk
from tkinter import ttk
from bod_import import BODImporter
from bod_db import bodDB

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        def changeText():
            try:
                text = BODImporter().captureBOD()
                stat_mes.delete(1.0,"end")
                stat_mes.insert(tk.END, 'BOD found: ' + text)
                
                # typVar.set(text.split()[0])
                qtyVar.set(text.split()[-1])
            except:
                stat_mes.delete(1.0,"end")
                stat_mes.insert(tk.END, 'Not BOD found, is the BOD visible on screen?')

        def createNewDB():
            text = bodDB().createDB()
            stat_mes.delete(1.0,'end')
            stat_mes.insert(tk.END, text)

        def deleteCurDB():
            text = bodDB().deleteDB()
            stat_mes.delete(1.0,'end')
            stat_mes.insert(tk.END, text)

        # Create the root window
        self.title('BOD Manager')
        # self.geometry('680x200')
        self.style = ttk.Style(self)

        # Set theme
        self.style.theme_use(themename='alt')

        # Create import BOD button
        btn = ttk.Button(self, text = 'Import current BOD', command = changeText)
        btn.grid(column=0, row=1, padx=10, pady=10,  sticky='w')

        # Create new database button
        dbBtn = ttk.Button(self, text='Create new database', command = createNewDB)
        dbBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky="w")

        # Create delete database button
        dbBtnDel = ttk.Button(self, text = 'Delete database', command = deleteCurDB)
        dbBtnDel.grid(row = 0, column = 1, padx = 0, pady = 0, sticky="w")

        # Create text widget to hold BOD info
        # bod_info = tk.Text(self, height = 1, width = 80)
        # bod_info.grid(column=1, row=1, padx=10, pady=10, sticky='w')
        # bod_info.insert(tk.END, "")

        # Create text widget to print status messages
        stat_lab = tk.Label(self, text = 'Status:')
        stat_lab.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
        stat_mes = tk.Text(self, height = 1)
        stat_mes.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "w")

        # Create file Menu
        menu_bar = tk.Menu(self)
        self.config(menu = menu_bar)
        file_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label = "New database")

        # Dropdown menues

        # BOD type (tailor/smith)
        # typVar = tk.StringVar(self)
        # typChoices = { 'tailor', 'smith'}

        # typMenu = tk.OptionMenu(self, typVar, *typChoices)
        # tk.Label(self, text = "Choose BOD type").grid(row = 2, column = 0)
        # typMenu.grid(row = 2, column = 1)

        # Quantity
        qtyVar = tk.StringVar(self)
        qtyChoices = { 10, 15, 20 }

        qtyMenu = tk.OptionMenu(self, qtyVar, *qtyChoices)
        tk.Label(self, text = "Choose quantity").grid(row = 3, column = 0)
        qtyMenu.grid(row = 3, column = 1)





# if __name__ == "__main__":
#     # bodImporter = BODImporter()
#     gui = GUI()
#     gui.mainloop()