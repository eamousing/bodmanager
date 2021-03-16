import tkinter as tk
from tkinter import ttk
from bod_import import BODImporter
from bod_db import bodDB
from bod_import import bod_data
from bod_import import unique_bods


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        bod_info = [None] * 6

        def detect_bod():
            try:
                best_match = BODImporter().captureBOD()
                text = bod_data[best_match][0:6]
                stat_mes.delete(1.0, "end")
                stat_mes.insert(tk.END, "BOD found: " + " ".join(text))

                typVar.set(text[0])
                qtyVar.set(text[5])
                sTypVar.set(text[1])
                bod_info[2] = sTypVar.get()
                if text[2] == "":
                    material_var.set("iron")
                else:
                    material_var.set(text[2])
                name_var.set(text[4])
                quality_var.set(text[3])
            except:
                stat_mes.delete(1.0, "end")
                stat_mes.insert(tk.END, "BOD not found, is the BOD visible on screen?")

        def createNewDB():
            text = bodDB().createDB()
            stat_mes.delete(1.0, "end")
            stat_mes.insert(tk.END, text)

        def deleteCurDB():
            text = bodDB().deleteDB()
            stat_mes.delete(1.0, "end")
            stat_mes.insert(tk.END, text)

        def bod_file_import():
            stat_mes.delete(0.0, "end")
            stat_mes.insert(tk.END, "Feature not implemented yet")

        def print_var():
            bod_info[0] = typVar.get()
            bod_info[1] = sTypVar.get()
            bod_info[2] = quality_var.get()
            bod_info[3] = material_var.get()
            bod_info[4] = name_var.get()
            bod_info[5] = qtyVar.get()
            stat_mes.delete(0.0, "end")
            stat_mes.insert(tk.END, bod_info)

        # Create the root window
        self.title("BOD Manager")
        self.geometry("640x480")
        self.style = ttk.Style(self)

        # Set theme
        self.style.theme_use(themename="alt")

        # Create import BOD button
        btn = ttk.Button(self, text="Import current BOD", command=detect_bod)
        btn.grid(column=0, row=1, padx=10, pady=10, sticky="w")

        # Import from file button
        btn_bod_file = ttk.Button(
            self, text="Import BODS from file", command=bod_file_import
        )
        btn_bod_file.grid(column=1, row=1, padx=0, pady=0, sticky="w")

        # Create print bod button
        print_bod_btn = ttk.Button(self, text="Print BOD", command=print_var)
        print_bod_btn.grid(row=1, column=3, padx=10, pady=10)

        # Create new database button
        dbBtn = ttk.Button(self, text="Create new database", command=createNewDB)
        dbBtn.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Create delete database button
        dbBtnDel = ttk.Button(self, text="Delete database", command=deleteCurDB)
        dbBtnDel.grid(row=0, column=1, padx=0, pady=0, sticky="w")

        # Create text widget to hold BOD info
        # bod_info = tk.Text(self, height = 1, width = 80)
        # bod_info.grid(column=1, row=1, padx=10, pady=10, sticky='w')
        # bod_info.insert(tk.END, "")

        # Create text widget to print status messages
        stat_lab = tk.Label(self, text="Status:")
        # stat_lab.grid(row=8, column=0, padx=10, pady=10, sticky="w")
        stat_lab.place(x=10, y=450)
        stat_mes = tk.Text(self, height=1)
        stat_mes.place(x=70, y=450, width=560)
        # stat_mes.grid(row=9, column=0, padx=10, pady=10, columnspan=2,sticky="w")

        # Create file Menu
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New database")

        # Dropdown menues

        # BOD type (tailor/smith)
        typVar = tk.StringVar(self)
        typChoices = {"tailor", "smith"}

        typMenu = tk.OptionMenu(self, typVar, *typChoices)
        typMenu.config(width=14)
        tk.Label(self, text="Choose BOD type").grid(
            row=2, column=0, padx=10, sticky="w"
        )
        typMenu.grid(row=2, column=1)

        # BOD size type
        sTypVar = tk.StringVar(self)
        sTypChoices = {"sbod", "lbod"}

        sTypMenu = tk.OptionMenu(self, sTypVar, *sTypChoices)
        sTypMenu.config(width=14)
        tk.Label(self, text="Choose BOD size type").grid(
            row=3, column=0, padx=10, sticky="w"
        )
        sTypMenu.grid(row=3, column=1)

        # Exceptional/normal
        quality_var = tk.StringVar(self)
        quality_choices = {"exceptional", "normal"}

        quality_menu = tk.OptionMenu(self, quality_var, *quality_choices)
        quality_menu.config(width=14)
        tk.Label(self, text="Choose BOD quality").grid(
            row=4, column=0, padx=10, sticky="w"
        )
        quality_menu.grid(row=4, column=1)

        # Material
        material_var = tk.StringVar(self)
        material_choices = {
            "iron",
            "dull copper",
            "shadow iron",
            "copper",
            "bronze",
            "gold",
            "agapite",
            "verite",
            "valorite",
        }

        material_menu = tk.OptionMenu(self, material_var, *material_choices)
        material_menu.config(width=14)
        tk.Label(self, text="Choose material").grid(
            row=5, column=0, padx=10, sticky="w"
        )
        material_menu.grid(row=5, column=1)

        # Name
        name_var = tk.StringVar(self)
        name_choices = unique_bods

        name_menu = tk.OptionMenu(self, name_var, *name_choices)
        name_menu.config(width=14)
        tk.Label(self, text="Choose BOD name").grid(
            row=6, column=0, padx=10, sticky="w"
        )
        name_menu.grid(row=6, column=1)

        # Quantity
        qtyVar = tk.StringVar(self)
        qtyChoices = {10, 15, 20}

        qtyMenu = tk.OptionMenu(self, qtyVar, *qtyChoices)
        qtyMenu.config(width=14)
        tk.Label(self, text="Choose quantity").grid(
            row=7, column=0, padx=10, sticky="w"
        )
        qtyMenu.grid(row=7, column=1)


# if __name__ == "__main__":
#     # bodImporter = BODImporter()
#     gui = GUI()
#     gui.mainloop()
