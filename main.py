import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
  
from my_exceptions import *
from changes import changes

class Proghram:
    
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry('650x250')
        self.master.title('Program')
        self.file_names = []
        self.tree = ttk.Treeview(self.master)

    def open_file(self):
        try:
            filename = askopenfilename()
            if [filename] == [()]:
                return
            if filename in self.file_names:
                raise RecursionException()
            self.file_names.append(filename)
            self.refrash_tree()
        except RecursionException:
            messagebox.showerror('Repetition Error', 'You can select file only once')

    def entry_clear(self):
        self.text1Entry.delete(0, tk.END)
        self.text2Entry.delete(0, tk.END)
        self.text1Entry.insert(0, '')
        self.text2Entry.insert(0, '')
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.file_names.clear()

    def clear_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.file_names.clear()

    def delete_row(self):
        try:
            row = self.tree.selection()[0]
            self.tree.delete(row)
            self.file_names.remove(row)
        except IndexError:
            messagebox.showerror('Error', 'Error nothing to delete')

    def save_changes(self):
        try:
            text1 = self.text1Entry.get()
            text2 = self.text2Entry.get()
            changes(self.file_names, text1, text2)
            self.file_names.clear()
            messagebox.showinfo('OK!', 'OK!')
            self.entry_clear()
        except ChoiceError:
            messagebox.showerror('Choice Error', 'Choose files!')
            
    def refrash_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in self.file_names:
            self.tree.insert(parent='', index='end', iid=row,text='', values=(row,), tag='orow')
        self.tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
        self.tree.grid(row=4, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

    def main_loop(self):
        button_choose = Button(self.master, text='Chooce file', command=self.open_file)
        button_save = Button(self.master, text='Replace text 1 to text 2', command=self.save_changes)
        button_clear = Button(self.master, text='Clear', command=self.clear_table)
        button_delete = Button(self.master, text='Delete', command=self.delete_row)
        text1Label = Label(self.master, text='Text 1:', width=10)
        self.text1Entry = Entry(self.master, width=10)
        text2Label = Label(self.master, text='Text 2:', width=10)
        self.text2Entry = Entry(self.master, width=10)

        button_choose.grid(row=2, column=0)
        button_save.grid(row=2, column=4)
        button_clear.grid(row=2, column=1)
        button_delete.grid(row=2, column=2)
        text1Label.grid(row=3, column=0)
        self.text1Entry.grid(row=3, column=1)
        text2Label.grid(row=3, column=2)
        self.text2Entry.grid(row=3, column=3)

        self.tree['columns'] = ('path',)
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('path', anchor=W, width=600)
        self.tree.heading('path', text="path", anchor=W)
        self.refrash_tree()
        self.master.mainloop()


if __name__ == '__main__':
    program = Proghram()
    program.main_loop()
