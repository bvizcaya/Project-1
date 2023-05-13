from tkinter import *
import csv

class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Project Name:')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)

        self.frame_date = Frame(self.window)
        self.label_date = Label(self.frame_date, text='Date:        ')
        self.entry_date = Entry(self.frame_date)
        self.label_date.pack(padx=5, side='left')
        self.entry_date.pack(padx=15, side='left')
        self.frame_date.pack(anchor='w', pady=10)

        self.frame_hoursworked = Frame(self.window)
        self.label_hoursworked = Label(self.frame_hoursworked, text='Hours Worked:')
        self.entry_hoursworked = Entry(self.frame_hoursworked)
        self.label_hoursworked.pack(padx=5, side='left')
        self.entry_hoursworked.pack(padx=5, side='left')
        self.frame_hoursworked.pack(anchor='w', pady=10)

        self.frame_summary = Frame(self.window)
        self.label_summary = Label(self.frame_summary, text='Summary:')
        self.entry_summary = Entry(self.frame_summary)
        self.label_summary.pack(padx=5, side='left')
        self.entry_summary.pack(padx=5, side='left')
        self.frame_summary.pack(anchor='w', pady=10)

        self.frame_savebutton = Frame(self.window)
        self.button_save = Button(self.frame_savebutton, text='SAVE', command=self.clicked)
        self.button_save.pack(padx=5, side='left')
        self.frame_savebutton.pack(anchor='c', pady=10)

    def clicked(self):
        name = self.entry_name.get()
        date = self.entry_date.get()
        hoursworked = self.entry_hoursworked.get()
        summary = self.entry_summary.get()

        with open('timesheet.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, date, hoursworked, summary])

        self.entry_name.delete(0, END)
        self.entry_date.delete(0, END)
        self.entry_hoursworked.delete(0, END)
        self.entry_summary.delete(0, END)
        self.entry_name.focus_set()