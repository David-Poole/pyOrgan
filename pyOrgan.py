# ############################################################################################################
# import statements
# ############################################################################################################
# ------------------------------------------------------------------------------------------------------------
# python library
# ------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from configparser import ConfigParser
import os
# ------------------------------------------------------------------------------------------------------------
# downloaded imports
# ------------------------------------------------------------------------------------------------------------
from PIL import Image, ImageTk


# ############################################################################################################
# User Interface
# ############################################################################################################
# ************************************************************************************************************
# Main Window
# ************************************************************************************************************
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        # set full screen
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f'{w}x{h}+0+0')
        # main menu
        self.menu = tk.Menu(master=self)
        # settings menu
        self.settings_show = tk.BooleanVar()
        self.menu.add_checkbutton(
            label='Settings',
            variable=self.settings_show,
            command=self.keyboard_settings,
            hidemargin=True
        )
        ## add menu to main window
        self.configure(menu=self.menu)
        # settings toggle
        # gui forms
        self.keyboardsettings = KeyboardSettingsForm(master=self)
    
    def keyboard_settings(self):
        #print(self.settings_show.get())
        if self.settings_show.get():
            self.keyboardsettings.grid(
                column=0,
                row=0
            )
        elif not self.settings_show.get():
            self.keyboardsettings.grid_forget()


# ************************************************************************************************************
# Keyboards
# ************************************************************************************************************
# Key Class
class Key(tk.Button):
    def __init__(self, master, keyboardtype, theme, keytype):
        super().__init__(master)
        # parameters
        self.keyboardtype = keyboardtype
        self.theme = theme
        self.keytype=keytype
        # button configuration
        self.note_off()
        self.image_update()
        self.config(command=self.state_update)

    def image_update(self):
        """updates the look of the button"""
        image_file = f'images/{self.keyboardtype}/{self.theme}/{self.keytype}.png'
        image = Image.open(image_file)
        self.image = ImageTk.PhotoImage(image=image)
        self.config(image=self.image)

    def theme_update(self, theme):
        """Update the look of the key based on the supplied theme"""
        self.theme = theme
        self.image_update()

    def note_off(self):
        """configure the key for NOTE-OFF"""
        self.state = "NOTE-OFF"
        self.config(relief='raised')

    def note_on(self):
        """configure the key for NOTE-ON"""
        self.state = "NOTE-ON"
        self.config(relief='flat')
    
    def state_update(self):
        """executes when the state of the key changes"""
        if self.state == 'NOTE-OFF':
            self.note_on()
        else:
            self.note_off()


# Manual Class
class Manual(tk.Frame):
    def __init__(self, master, theme):
        super().__init__(master)
        # create 'natural' keys:
        naturals = tuple(
            Key(master=self,
                keyboardtype='manual',
                theme=theme,
                keytype='natural') for i in range(36)
        )
        # create 'accidental' keys:
        accidentals = tuple(
            Key(master=self, 
                keyboardtype='manual', 
                theme=theme, 
                keytype='accidental') for i in range(25)
        )
        # arrange keys in an accessible tuple
        self.keys = (
            naturals[0], accidentals[0], naturals[1], accidentals[1], naturals[2], naturals[3], 
            accidentals[2], naturals[4], accidentals[3], naturals[5], accidentals[4], naturals[6], 
            naturals[7], accidentals[5], naturals[8], accidentals[6], naturals[9], naturals[10],
            accidentals[7], naturals[11], accidentals[8], naturals[12], accidentals[9], naturals[13],
            naturals[14], accidentals[10], naturals[15], accidentals[11], naturals[16], naturals[17],
            accidentals[12], naturals[18], accidentals[13], naturals[19], accidentals[14], naturals[20],
            naturals[21], accidentals[15], naturals[22], accidentals[16], naturals[23], naturals[24],
            accidentals[17], naturals[25], accidentals[18], naturals[26], accidentals[19], naturals[27],
            naturals[28], accidentals[20], naturals[29], accidentals[21], naturals[30], naturals[31],
            accidentals[22], naturals[32], accidentals[23], naturals[33], accidentals[24], naturals[34],
            naturals[35],
        )
        # layout keys
        for key in naturals:
            key.pack(side='left')
        xpositions = (
            9, 25, 57, 73, 89, 121, 137, 169, 185, 201, 233, 249, 281,
            297, 313, 345, 361, 393, 409, 425, 457, 473, 505, 521, 537
        )
        for key, x in zip(accidentals, xpositions):
            key.place(x=x)
    
    def theme_update(self, theme):
        """update the look of the organ manual"""
        for key in self.keys:
            key.theme_update(theme=theme)


# Pedalboard Class
class Pedalboard(tk.Frame):
    def __init__(self, master, theme):
        super().__init__(master)
        # create pedals
        self.pedals = (
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='accidental'),
            Key(master=self, 
                keyboardtype='pedalboard', 
                theme=theme, 
                keytype='natural')
        )
        # layout pedals
        for pedal in self.pedals:
            pedal.pack(
                side='left',
                anchor='n'
            )
    
    def theme_update(self, theme):
        """update the look of the organ pedalboard"""
        for pedal in self.pedals:
            pedal.theme_update(theme=theme)


# ************************************************************************************************************
# Pistons
# ************************************************************************************************************
# Piston Class
class Piston(tk.Frame):
    def __init__(self, master, theme, diameter, text):
        super().__init__(master)
        # parameters
        self.theme = theme
        self.diameter = diameter
        self.text = text
        # create button
        self.button = tk.Button(master=self)
        self.button.pack()
        # configure piston
        self.state_off()
        self.image_update()
        self.button.config(command=self.state_update)
        self.pack_propagate(0)

    def image_update(self):
        """update the button image"""
        image_file = f'images/piston/{self.theme}/{self.state}.png'
        image = Image.open(image_file)
        image = image.resize((self.diameter, self.diameter), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(image=image)
        self.button.config(
            compound=tk.CENTER,
            image=self.image, 
            text=self.text,
            bd=0)
        self.config(
            width=self.diameter+2,
            height=self.diameter+2
        )

    def theme_update(self, theme):
        self.theme = theme
        self.image_update()

    def state_off(self):
        self.state = 'off'
        self.image_update()

    def state_on(self):
        self.state = 'on'
        self.image_update()

    def state_update(self):
        if self.state == 'off':
            self.state_on()
        else:
            self.state_off()


# ************************************************************************************************************
# Organ Console
# ************************************************************************************************************

# ************************************************************************************************************
# User Forms
# ************************************************************************************************************
# Keyboard Settings
class KeyboardSettingsForm(ttk.Frame):
    labelwidth = 20
    def __init__(self, master):
        super().__init__(master)
        # Config Parser ......................................................................................
        self.configfile = 'pyOrgan.cfg' 
        self.parser = ConfigParser()
        # General Keyboard Settings ..........................................................................
        self.generalkeyboardsettings = ttk.LabelFrame(
            master=self,
            text="General Keyboard Settings",
            labelanchor='n',
        )
        # Manual Settings ....................................................................................
        self.manualsettings = ttk.LabelFrame(
            master=self.generalkeyboardsettings,
            text="General Manual Settings",
            labelanchor='nw',
        )
        # number of manuals
        self.numbermanuals = tk.StringVar()
        self.numbermanuals_label = ttk.Label(
            master=self.manualsettings,
            text="Number of Manuals:",
            width=self.labelwidth
        )
        self.numbermanuals_spin = ttk.Spinbox(
            master=self.manualsettings,
            textvariable=self.numbermanuals,
            from_=1,
            to=5,
            width=1,
            justify='center',
            command=self.numbermanuals_update
        )
        # manuals theme
        manualthemes = os.listdir('images/manual/')
        self.manualstheme = tk.StringVar()
        self.manualstheme_label = ttk.Label(
            master=self.manualsettings,
            text="Manuals Theme:",
            width=self.labelwidth
        )
        self.manualstheme_combo = ttk.Combobox(
            master=self.manualsettings,
            textvariable=self.manualstheme,
            values=manualthemes,
            justify='center'
        )
        # thumb piston diameter
        self.thumbpistondiameter = tk.StringVar()
        self.thumbpistondiameter_label = ttk.Label(
            master=self.manualsettings,
            text="Thumb Piston Diameter:",
            width=self.labelwidth
        )
        self.thumbpistondiameter_spin = ttk.Spinbox(
            master=self.manualsettings,
            textvariable=self.thumbpistondiameter,
            width=2,
            justify='center',
            from_=10,
            to=30,
            command=self.configfile_organ_update
        )
        # thumb piston theme
        pistonthemes = os.listdir('images/piston/')
        self.thumbpistontheme = tk.StringVar()
        self.thumbpistontheme_label = ttk.Label(
            master=self.manualsettings,
            text="Thumb Piston Theme:",
            width=self.labelwidth
        )
        self.thumbpistontheme_combo = ttk.Combobox(
            master=self.manualsettings,
            textvariable=self.thumbpistontheme,
            values=pistonthemes,
            justify='center'
        )
        # Pedalboard Settings ................................................................................
        self.pedalboardsettings = ttk.LabelFrame(
            master=self.generalkeyboardsettings,
            text="Pedalboard Settings",
            labelanchor='nw'
        )
        # include pedalboard
        self.includepedalboard = tk.BooleanVar()
        self.includepedalboard_label = ttk.Label(
            master=self.pedalboardsettings,
            text="Include Pedalboard:",
            width=self.labelwidth
        )
        self.includepedalboard_check = ttk.Checkbutton(
            master=self.pedalboardsettings,
            variable=self.includepedalboard,
            command=self.numbermanuals_update
        )
        # pedalboard theme
        pedalboardthemes = os.listdir('images/pedalboard/')
        self.pedalboardtheme = tk.StringVar()
        self.pedalboardtheme_label = ttk.Label(
            master=self.pedalboardsettings,
            text="Pedalboard Theme:",
            width=self.labelwidth
        )
        self.pedalboardtheme_combo = ttk.Combobox(
            master=self.pedalboardsettings,
            textvariable=self.pedalboardtheme,
            values=pedalboardthemes,
            justify='center'
        )
        # toepiston diameter
        self.toepistondiameter = tk.StringVar()
        self.toepistondiameter_label = ttk.Label(
            master=self.pedalboardsettings,
            text="Toe Piston Diameter",
            width=self.labelwidth
        )
        self.toepistondiameter_spin = ttk.Spinbox(
            master=self.pedalboardsettings,
            textvariable=self.toepistondiameter,
            from_=10,
            to=50,
            width=2,
            justify='center',
            command=self.configfile_organ_update
        )
        # toepiston theme
        self.toepistontheme = tk.StringVar()
        self.toepistontheme_label = ttk.Label(
            master=self.pedalboardsettings,
            text="Toe Piston Theme:",
            width=self.labelwidth
        )
        self.toepistontheme_combo = ttk.Combobox(
            master=self.pedalboardsettings,
            textvariable=self.toepistontheme,
            values=pistonthemes,
            justify='center'
        )
        # combobox commands
        comboboxes = (
            self.manualstheme_combo, self.thumbpistontheme_combo, self.pedalboardtheme_combo, 
            self.toepistontheme_combo
        )
        for combobox in comboboxes:
            combobox.bind('<<ComboboxSelected>>', self.configfile_organ_update)
        # Layout .............................................................................................
        manualsettings_widgets = (
            (self.numbermanuals_label, self.numbermanuals_spin),
            (self.manualstheme_label, self.manualstheme_combo),
            (self.thumbpistondiameter_label, self.thumbpistondiameter_spin),
            (self.thumbpistontheme_label, self.thumbpistontheme_combo)
        )
        for i in range(len(manualsettings_widgets)):
            for x in range(len(manualsettings_widgets[i])):
                manualsettings_widgets[i][x].grid(
                    column=x,
                    row=i,
                    padx=2,
                    pady=2,
                    sticky='w'
                )
        pedalboardsettings_widgets = (
            (self.includepedalboard_label, self.includepedalboard_check),
            (self.pedalboardtheme_label, self.pedalboardtheme_combo),
            (self.toepistondiameter_label, self.toepistondiameter_spin),
            (self.toepistontheme_label, self.toepistontheme_combo)
        )
        for i in range(len(pedalboardsettings_widgets)):
            for x in range(len(pedalboardsettings_widgets[i])):
                pedalboardsettings_widgets[i][x].grid(
                    column=x,
                    row=i,
                    padx=2,
                    pady=2,
                    sticky='w'
                )
        frames = (self.manualsettings, self.pedalboardsettings)
        for frame in frames:
            frame.pack(
                anchor='nw',
                padx=5,
                pady=(0, 5)
            )
        # Keyboard Settings ..................................................................................
        self.keyboardsettings = ttk.LabelFrame(
            master=self,
            text="Keyboard Settings",
            labelanchor='nw',
        )
        # keyboard
        self.keyboard = tk.StringVar()
        self.keyboard_label = ttk.Label(
            master=self.keyboardsettings,
            text="Keyboard:",
            width=self.labelwidth
        )
        self.keyboard_combo = ttk.Combobox(
            master=self.keyboardsettings,
            textvariable=self.keyboard,
        )
        self.keyboard_combo.bind('<<ComboboxSelected>>', self.keyboardsettings_populate)
        # organ division
        divisions = ("PEDAL", "GREAT", "SWELL", "CHOIR", "SOLO", "ECHO")
        self.division = tk.StringVar()
        self.division_label = ttk.Label(
            master=self.keyboardsettings,
            text="Organ Division:",
            width=self.labelwidth
        )
        self.division_combo = ttk.Combobox(
            master=self.keyboardsettings,
            textvariable=self.division,
            values=divisions,
            justify='center',
            state='disabled'
        )
        self.division_combo.bind('<<ComboboxSelected>>', self.configfile_keyboard_update)
        # include presets
        self.includepresets = tk.BooleanVar()
        self.includepresets_label = ttk.Label(
            master=self.keyboardsettings,
            text="Include Presets:",
            width=self.labelwidth
        )
        self.includepresets_check = ttk.Checkbutton(
            master=self.keyboardsettings,
            variable=self.includepresets,
            command=self.configfile_keyboard_update,
            state='disabled'
        )
        # Keyboard Presets ...................................................................................
        self.keyboardpresets = ttk.LabelFrame(
            master=self.keyboardsettings,
            text='Keyboard Presets',
            labelanchor='nw'
        )
        # include generals
        self.includegenerals = tk.BooleanVar()
        self.includegenerals_label = ttk.Label(
            master=self.keyboardpresets,
            text="Include Generals:",
            width=self.labelwidth
        )
        self.includegenerals_check = ttk.Checkbutton(
            master=self.keyboardpresets,
            variable=self.includegenerals,
            command=self.configfile_keyboard_update,
            state='disabled'
        )
        # number of generals
        self.numbergenerals = tk.StringVar()
        self.numbergenerals_label = ttk.Label(
            master=self.keyboardpresets,
            text="Number of Generals:",
            width=self.labelwidth
        )
        self.numbergenerals_spin = ttk.Spinbox(
            master=self.keyboardpresets,
            textvariable=self.numbergenerals,
            width=2,
            justify='center',
            command=self.configfile_keyboard_update,
            state='disabled'
        )
        # include divisionals
        self.includedivisionals = tk.BooleanVar()
        self.includedivisionals_label = ttk.Label(
            master=self.keyboardpresets,
            text="Include Divisionals:",
            width=self.labelwidth
        )
        self.includedivisionals_check = ttk.Checkbutton(
            master=self.keyboardpresets,
            variable=self.includedivisionals,
            command=self.configfile_keyboard_update,
            state='disabled'
        )
        # number of divisionals
        self.numberdivisionals = tk.StringVar()
        self.numberdivisionals_label = ttk.Label(
            master=self.keyboardpresets,
            text="Number of Divisionals:",
            width=self.labelwidth
        )
        self.numberdivisionals_spin = ttk.Spinbox(
            master=self.keyboardpresets,
            textvariable=self.numberdivisionals,
            width=2,
            justify='center',
            command=self.configfile_keyboard_update,
            state='disabled'
        )
        # Layout .............................................................................................
        keyboardsettings_widgets = (
            (self.keyboard_label, self.keyboard_combo),
            (self.division_label, self.division_combo),
            (self.includepresets_label, self.includepresets_check),
            self.keyboardpresets
        )
        for i in range(len(keyboardsettings_widgets)):
            try:
                for x in range(len(keyboardsettings_widgets[i])):
                    keyboardsettings_widgets[i][x].grid(
                        column=x,
                        row=i,
                        padx=2,
                        pady=2,
                        sticky='w'
                    )
            except:
                keyboardsettings_widgets[i].grid(
                    column=0,
                    columnspan=2,
                    row=i,
                    padx=10,
                    pady=(5 ,2),
                    sticky='w'
                )
        keyboardpreset_widgets = (
            (self.includegenerals_label, self.includegenerals_check),
            (self.numbergenerals_label, self.numbergenerals_spin),
            (self.includedivisionals_label, self.includedivisionals_check),
            (self.numberdivisionals_label, self.numberdivisionals_spin)
        )
        for i in range(len(keyboardpreset_widgets)):
            for x in range(len(keyboardpreset_widgets[i])):
                keyboardpreset_widgets[i][x].grid(
                    column=x,
                    row=i,
                    padx=2,
                    pady=2,
                    sticky='w'
                )
        forms = (self.generalkeyboardsettings, self.keyboardsettings)
        for form in forms:
            form.pack(
                anchor='w',
                padx=2,
                pady=(0, 10),
                ipadx=5,
                ipady=5
            )
        # Configure Form Data
        self.populate_form()
        self.keyboardsettings_configure()

    def populate_form(self):
        self.parser.read(filenames=self.configfile)
        self.numbermanuals.set(self.parser['Organ']['number_manuals'])
        self.manualstheme.set(self.parser['Organ']['manuals_theme'])
        self.thumbpistondiameter.set(self.parser['Organ']['thumb_piston_diameter'])
        self.thumbpistontheme.set(self.parser['Organ']['thumb_piston_theme'])
        self.includepedalboard.set(self.parser['Organ']['include_pedalboard'])
        self.pedalboardtheme.set(self.parser['Organ']['pedalboard_theme'])
        self.toepistondiameter.set(self.parser['Organ']['toe_piston_diameter'])
        self.toepistontheme.set(self.parser['Organ']['toe_piston_theme'])

    def keyboardsettings_configure(self):
        keyboards = [f"Manual {x+1}" for x in range(int(self.numbermanuals.get()))]
        if self.includepedalboard.get() == True:
            keyboards.append("Pedalboard")
        self.keyboard_combo.config(values=keyboards)

    def set_empty_keyboard(self):
        self.parser.read(self.configfile)
        for i in range(int(self.numbermanuals.get()), 5):
            self.parser[f'Manual {i+1}']['organ_division'] = 'None'
            self.parser[f'Manual {i+1}']['include_pistons'] = 'False'
            self.parser[f'Manual {i+1}']['include_generals'] ='False'
            self.parser[f'Manual {i+1}']['number_generals'] = '0'
            self.parser[f'Manual {i+1}']['include_divisionals'] = 'False'
            self.parser[f'Manual {i+1}']['number_divisionals'] = '0'
        if self.includepedalboard.get() == False:
            self.parser['Organ']['pedalboard_theme'] = 'None'
            self.parser['Pedalboard']['organ_division'] = 'None'
            self.parser['Pedalboard']['include_pistons'] = 'False'
            self.parser['Pedalboard']['include_generals'] = 'False'
            self.parser['Pedalboard']['number_generals'] = '0'
            self.parser['Pedalboard']['include_divisionals'] = 'False'
            self.parser['Pedalboard']['number_divisionals'] = '0'
        else:
            self.parser['Organ']['pedalboard_theme'] = 'default'
            self.parser['Pedalboard']['organ_division'] = 'PEDALS'
        self.configfile_write()

    def keyboardsettings_populate(self, event=None):
        # activate form
        self.division_combo.config(state='normal')
        self.includepresets_check.config(state='normal')
        self.includegenerals_check.config(state='normal')
        self.numbergenerals_spin.config(state='normal')
        self.includedivisionals_check.config(state='normal')
        self.numberdivisionals_spin.config(state='normal')
        # populate form
        self.parser.read(filenames=self.configfile)
        keyboard = self.keyboard.get()
        self.division.set(self.parser[keyboard]['organ_division'])
        self.includepresets.set(self.parser[keyboard]['include_pistons'])
        self.includegenerals.set(self.parser[keyboard]['include_generals'])
        self.numbergenerals.set(self.parser[keyboard]['number_generals'])
        self.includedivisionals.set(self.parser[keyboard]['include_divisionals'])
        self.numberdivisionals.set(self.parser[keyboard]['number_divisionals'])

    def configfile_organ_update(self, event=None):
        self.parser.read(filenames=self.configfile)
        self.parser['Organ']['number_manuals'] = self.numbermanuals.get()
        self.parser['Organ']['manuals_theme'] = self.manualstheme.get()
        self.parser['Organ']['thumb_piston_diameter'] = self.thumbpistondiameter.get()
        self.parser['Organ']['thumb_piston_theme'] = self.thumbpistontheme.get()
        self.parser['Organ']['include_pedalboard'] = str(self.includepedalboard.get())
        self.parser['Organ']['pedalboard_theme'] = self.pedalboardtheme.get()
        self.parser['Organ']['toe_piston_diameter'] = self.toepistondiameter.get()
        self.parser['Organ']['toe_piston_theme'] = self.toepistontheme.get()
        self.configfile_write()

    def configfile_keyboard_update(self, event=None):
        self.parser.read(filenames=self.configfile)
        keyboard = self.keyboard.get()
        self.parser[keyboard]['organ_division'] = str(self.division.get())
        self.parser[keyboard]['include_pistons'] = str(self.includepresets.get())
        self.parser[keyboard]['include_generals'] = str(self.includegenerals.get())
        self.parser[keyboard]['number_generals'] = str(self.numbergenerals.get())
        self.parser[keyboard]['include_divisionals'] = str(self.includedivisionals.get())
        self.parser[keyboard]['number_divisionals'] = str(self.numberdivisionals.get())
        self.configfile_write()

    def configfile_write(self):
        with open(self.configfile, 'w') as configfile:
            self.parser.write(configfile)

    def numbermanuals_update(self):
        self.configfile_organ_update()
        self.keyboardsettings_configure()
        self.set_empty_keyboard()


# Run Module:
# ____________________________________________________________________________________________________________
if __name__ == '__main__':
    mainwindow = MainWindow()
    mainwindow.mainloop()
