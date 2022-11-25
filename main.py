from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Клининговая компания "ПЫЛИНКА"') #name window
root.geometry('735x470') #size window
root.resizable(width=False, height=False)
root['bg'] = 'hot pink'

my_tree = ttk.Treeview(root)

#define our columns
my_tree['columns'] = ("Имя сотрудника", "Объект", "Время начала уборки", "Время конца уборки")

# formate our columns
my_tree.column("#0", width=115, minwidth=25)
my_tree.column("Имя сотрудника", anchor=W, width=110)
my_tree.column("Объект", anchor=CENTER, width=180)
my_tree.column("Время начала уборки", anchor=W, width=150)
my_tree.column("Время конца уборки", anchor=W, width=150)

#CREATE HADDINGS
my_tree.heading("#0", text="Номер сотрудника", anchor=W)
my_tree.heading("Имя сотрудника", text="Имя сотрудника", anchor=W)
my_tree.heading("Объект", text="Объект", anchor=CENTER)
my_tree.heading("Время начала уборки", text="Время начала уборки", anchor=W)
my_tree.heading("Время конца уборки", text="Время конца уборки", anchor=W)

#add data
data = [('1','Нино', 'Дом', '15:00', '18:00'),
       ('2','Лиа', 'Дом', '12:00', '16:00'),
       ('3','Сониа', 'Дом', '10:45', '12:30')]

global count
count=0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4]))
    count += 1

#my_tree.insert(parent='', index='end', iid=0, text="1", values=("Нино М.", "Загородный дом", "12:10", "15:30"))
#my_tree.insert(parent='', index='end', iid=1, text="2", values=("Гавриил Г.", "Квартира", "12:10", "15:30"))
#my_tree.insert(parent='', index='end', iid=2, text="3", values=("Зинаида Р.", "Загородный дом", "12:10", "15:30"))
#my_tree.insert(parent='', index='end', iid=3, text="4", values=("Леопольд И.", "Этаж дома", "12:10", "15:30"))
#my_tree.insert(parent='', index='end', iid=4, text="5", values=("Сониа Ф.", "Гостиница", "12:10", "15:30"))
#my_tree.insert(parent='', index='end', iid=5, text="6", values=("Вера С.", "Квартира", "12:10", "15:30"))

#pack to the screen
my_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)

#Labels
nl = Label(add_frame, text="Номер сотрудника")
nl.grid(row=0, column=0)

il = Label(add_frame, text="Имя сотрудника")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Объект")
tl.grid(row=0, column=2)

tl = Label(add_frame, text="Время начала уборки")
tl.grid(row=0, column=3)

tl = Label(add_frame, text="Время конца уборки")
tl.grid(row=0, column=4)


#entry boxes
number_box = Entry(add_frame)
number_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

rm_box = Entry(add_frame)
rm_box.grid(row=1, column=3)

fm_box = Entry(add_frame)
fm_box.grid(row=1, column=4)

#add record
def add_record():
    global count
    my_tree.insert(parent='', index='end', iid=count, text="1", values=(number_box.get(), id_box.get(), topping_box.get(), rm_box.get(), fm_box.get()))
    count += 1

#clear the boxes
    number_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)
    rm_box.delete(0, END)
    fm_box.delete(0, END)

#remove all records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


#buttons
add_record = Button(root, text="Добавить сотрудника", command=add_record)
add_record.pack(pady=20)

#remove all
remove_all = Button(root, text="Удалить все записи", command=remove_all)
remove_all.pack(pady=10)

root.mainloop()


