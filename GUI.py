import tkinter as tk
from tkinter import messagebox

title = 'LessMess by Vladyslav Pukhliak'
window = tk.Tk()

class MessageBoxUtils:
    def init():
        window.withdraw()

    def destroy():
        window.destroy()

    def allowed_renaming(n):
        return messagebox.askyesno(
            f'{title} — Some files were skipped',
            f'There are {n} files that couldn\'t be moved to other directories\n' +
            'because files with the same name already exist.\n\n' +
            f'Allow {title} to add the "_duplicate" ending to their names?',
            icon='warning')

    def show_success():
        messagebox.showinfo(
            title,
            'Your files have been successfully\n' +
            'renamed and organised.')
