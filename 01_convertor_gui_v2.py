from tkinter import *

class Converter:
    
    def __init__(self): # Initialized

        # Initialize variables
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = BooleanVar()
        self.var_has_error.set(False)

        # common format for all buttons
        #Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#fff"

        # Set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
            text="Temperature Converter",
            font=("Arial", "16", "bold")
        )
        self.temp_heading.grid(row=0)

        # Instructions
        instructions = "Please enter a temperature below and then press one of the buttons to convert it from Centigrade to Fahrenheit."

        self.temp_instructions = Label(self.temp_frame,
        text=instructions,
        wrap=250, width=40,
        justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
            font=("Arial", "14")
        )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.output_label = Label(self.temp_frame, text="",
            fg="#9C0000"
        )
        self.output_label.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4, padx=5, pady=5)

        self.to_celsius_button = Button(self.button_frame,
            text="To Degrees C",
            font=button_font,
            bg="#909",
            fg=button_fg,
            width=12,

            command=self.to_celsius
        )
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_farenheit_button = Button(self.button_frame,
            text="To Farenheit",
            font=button_font,
            bg="#090",
            fg=button_fg,
            width=12,
        )
        self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame,
            text="Help / Info",
            font=button_font,
            bg="#c60",
            fg=button_fg,
            width=12,
        )
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_history_button = Button(self.button_frame,
            text="History / Export",
            font=button_font,
            bg="#004C99",
            fg=button_fg,
            width=12,
            state=DISABLED,
        )
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

    # Checks user input and if it's valid, converts temperature
    def check_temp(self,min_value):

        has_error = False
        error = "Please enter a number that is more than {}".format(min_value)

        response = self.temp_entry.get()

        try:
            response = float(response)

            if response < min_value:
                has_error = True

        except ValueError:
            has_error = True

        # Sets var_has_error so that entrybox and
        # Labels can be correctly formatted by formatting function
        if has_error:
            self.var_has_error.set(True)
            self.var_feedback.set(error)
            return "invalid"

        # If we have no errors...
        else:
            # Set to False in case of previous errors
            self.var_has_error.set(False)

            # Return number to be
            # Converted and enable history button
            self.to_history_button.config(state=NORMAL)
            return response

    def to_celsius(self):
        to_convert = self.check_temp(-459)

        if to_convert != "invalid":
            # do calculation
            self.var_feedback.set("Converting {} to C :)".format(to_convert))

        self.output_answer()

    def to_fahrenheit(self):
        to_convert = self.check_temp(-273)

        if to_convert != "invalid":
            # do calculation
            self.var_feedback.set("Converting {} to F :)".format(to_convert))

    # Shows user output and clears entry widget
    # ready for next calculation
    def output_answer(self):
        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors:
            # red text, pink entry box
            self.output_label.config(fg="#9C0000")
            self.temp_entry.config(bg="#F8CECC")
        else:
            self.output_label.config(fg="#004C00")
            self.temp_entry.config(bg="#FFFFFF")

        self.output_label.config(text=output)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
