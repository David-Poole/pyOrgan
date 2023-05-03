import tkinter as tk
from tkinter import ttk
from ui.ui_settings import SettingsMenu


# ************************************************************************************************************
# Main Window
# ************************************************************************************************************
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        # set title
        self.title("pyOrgan")
        # set full screen
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f'{w}x{h}+0+0')
        # main menu
        self.menu = tk.Menu(master=self)
        # view menu
        self.view_menu = tk.Menu(
            master=self.menu,
            tearoff=False
        )
        # left side options form
        self.settings_show = tk.BooleanVar()
        self.view_menu.add_checkbutton(
            label='Keyboard Settings',
            variable=self.settings_show,
            command=self.settings_toggle,
        )
        # add menus to main menu
        self.menu.add_cascade(label='view', menu=self.view_menu)
        # add menu to main window
        self.configure(menu=self.menu)
        # settings toggle
        # gui forms
        self.settings = SettingsMenu(master=self)
    
    def settings_toggle(self):
        #print(self.settings_show.get())
        if self.settings_show.get():
            self.settings.grid(
                column=0,
                row=0
            )
        elif not self.settings_show.get():
            self.settings.grid_forget()