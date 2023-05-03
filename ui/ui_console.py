import tkinter as tk
from PIL import Image, ImageTk


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


# Presets Class
class Presets(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


# ************************************************************************************************************
# Organ Console
# ************************************************************************************************************
