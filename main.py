from guifinal import *

def main():
    window = Tk()
    window.title('Timesheet')
    window.geometry('250x200')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()
