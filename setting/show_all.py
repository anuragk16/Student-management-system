from tkinter import *
from tkinter import Toplevel
from setting.load_and_save import *
from tkinter.ttk import Treeview

def heading_click():
    head_ = Toplevel()
    head_.geometry("1000x500+200+200")
    head_.grab_set()
    head_.resizable(False,False)
    head_.iconbitmap("setting\\assets\\icon.ico")
    head_.config(bg="black")

    treev = Treeview(head_, selectmode ='browse')
    treev.place(x=0 , y=0 , width=1000 , height=490)
    treev["columns"] = ('rollno', 'name', 'mob', 'dob', 'gender', 'email', 'address')
    treev['show'] = 'headings'

    treev.heading('rollno', text='R.No.')
    treev.heading('name', text='Name')
    treev.heading('mob', text='MOB.')
    treev.heading('dob', text='DOB')
    treev.heading('gender', text='Gender')  
    treev.heading('email', text='Email')
    treev.heading('address', text='address')

    treev.column("rollno", width = 40, anchor ='w')
    treev.column("name", width = 150, anchor ='w')
    treev.column("mob", width = 160, anchor ='w')
    treev.column("dob", width = 150, anchor ='w')
    treev.column("gender", width = 60, anchor ='w')
    treev.column("email", width = 200, anchor ='w')
    treev.column("address", width = 220, anchor ='w')

    all_list_ = np.load("DATA.npy")
    num_splite = len(all_list_)
    for_show = np.vsplit(all_list_,num_splite)
    for i in range(0,num_splite-2):
        file = str(for_show[i+2])
        gap = "_'"
        gap1 = " "
        for k in range(0,len(file)):
            if gap1 == file[k]:
                file = file.replace(gap1, '_')
        for k in range(0,6):
            file = file.replace("__'", " '")
            file = file.replace(gap, " '")
        treev.insert('',END,values=file)

def treeviewshow(master):
    global tree_view
    column = ('rollno', 'name', 'mob', 'dob', 'gender', 'email', 'address')
    tree_view = Treeview(master, show="headings", columns=column)
    tree_view.place(x=100 , y=350 , width=1000 , height=220)
 
    tree_view.heading('rollno', text='R.No.', command=lambda : heading_click())
    tree_view.heading('name', text='Name', command=lambda : heading_click())
    tree_view.heading('mob', text='MOB.', command=lambda : heading_click())
    tree_view.heading('dob', text='DOB', command=lambda : heading_click())
    tree_view.heading('gender', text='Gender', command=lambda : heading_click())  
    tree_view.heading('email', text='Email', command=lambda : heading_click())
    tree_view.heading('address', text='address', command=lambda : heading_click())

    tree_view.column("rollno", width = 40, anchor ='w')
    tree_view.column("name", width = 150, anchor ='w')
    tree_view.column("mob", width = 160, anchor ='w')
    tree_view.column("dob", width = 150, anchor ='w')
    tree_view.column("gender", width = 60, anchor ='w')
    tree_view.column("email", width = 200, anchor ='w')
    tree_view.column("address", width = 220, anchor ='w')
    tree_view['show'] = 'headings'

def show_all(master):
    treeviewshow(master)
    all_list_ = np.load("DATA.npy")
    num_splite = len(all_list_)
    for_show = np.vsplit(all_list_,num_splite)
    for i in range(0,num_splite-2):
        file = str(for_show[i+2])
        gap = "_'"
        gap1 = " "
        for k in range(0,len(file)):
            if gap1 == file[k]:
                file = file.replace(gap1, '_')
        for k in range(0,6):
            file = file.replace("__'", " '")
            file = file.replace(gap, " '")
        tree_view.insert('',END,values=file)
        







