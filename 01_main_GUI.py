from tkinter import *
from functools import partial  # to prevent unwanted windows

import random


class quiz:
    def __init__(self, parent):

        # Formatting variables...
        background_color = "#00b2ff"

        # convertor Main screen GUI...
        self.quiz_frame = Frame(width=300, height=300, bg=background_color, pady=10)
        self.quiz_frame.grid()



        # Temperature conversion heading (row 0)
        self.quiz_home_label = Label(self.quiz_frame, text="Genetics Quiz",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.quiz_home_label.grid(row=0)

        # help / start / history frame (row 3)
        self.help_start_hist_frame = Frame(self.quiz_frame, bg=background_color)
        self.help_start_hist_frame.grid(row=3, column=0)

        # help button
        self.help_button = Button(self.help_start_hist_frame, font="Arial 14", bg="#95B8FE",
                                  text="Help", width=8, command=self.help)
        self.help_button.grid(row=3, column=1)

        # start start button
        self.start_button = Button(self.help_start_hist_frame, text="Start",
                                   font=("Arial", "16", "bold"),
                                   bg="#0BB103", width="10")
        self.start_button.grid(row=3, column=2)

        # show history button
        self.history_button = Button(self.help_start_hist_frame, text="History", bg="#95B8FE",
                                     font=("Arial", "14"), width=8,)
        self.history_button.grid(row=3, column=3)

    # help GUI
    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __init__(self, partner):
        background = "#00b2ff"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (ie: help box)
        self.help_box = Toplevel()

        # if users press cross at top, close help and 'releases' help button
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help, partner))


        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                  font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="#72aeee", font="arial 14 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # make the help button go back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("quiz")
    something = quiz(root)
    root.mainloop()
