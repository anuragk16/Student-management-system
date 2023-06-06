from tkinter import Toplevel,messagebox
from tkinter import *
from tkinter.ttk import Treeview
from setting.load_and_save import  *
import numpy as np

def label(master, text="nothing", x=0, y=0):
    list_area = Label(master, text=text, bg="gray", font=("times of India",18,'bold'), fg="lightblue",)
    list_area.place(x=x, y=y)

def treeviewshow(master):
    global tree_view
    column = ('rollno', 'name', 'mob', 'dob', 'gender', 'email', 'address')
    tree_view = Treeview(master, show="headings", columns=column)
    tree_view.place(x=100 , y=350 , width=1000 , height=220)
 
    tree_view.heading('rollno', text='R.No.')
    tree_view.heading('name', text='Name')
    tree_view.heading('mob', text='MOB.')
    tree_view.heading('dob', text='DOB')
    tree_view.heading('gender', text='Gender')  
    tree_view.heading('email', text='Email')
    tree_view.heading('address', text='address')

    tree_view.column("rollno", width = 40, anchor ='w')
    tree_view.column("name", width = 150, anchor ='w')
    tree_view.column("mob", width = 160, anchor ='w')
    tree_view.column("dob", width = 150, anchor ='w')
    tree_view.column("gender", width = 60, anchor ='w')
    tree_view.column("email", width = 200, anchor ='w')
    tree_view.column("address", width = 220, anchor ='w')
    tree_view['show'] = 'headings'

def search_st(master):
    treeviewshow(master)
    try :
        seah_rollno = int(rollno_seah.get())
    except ValueError:
        seah_rollno = rollno_seah.get()

    seah_name = (str(name_seah.get())).upper()

    all_list_ = np.load("DATA.npy")
    
    rollno = list( all_list_[ :, 0])
    name = list( all_list_[ :, 1])

    '''
    lis = np.array([],dtype=object)
    if seah_rollno in rollno:
        index_no_to_remove = rollno.index(seah_rollno)
        all_list = np.delete(all_list_, index_no_to_remove, 0)
    print(all_list)
    '''

    if seah_rollno == "" and seah_name == "":
        messagebox.showerror(title="NO DATA", message="NO DATA FILL")

    elif seah_rollno in rollno and seah_rollno != "":
        index_no = rollno.index(seah_rollno)
        all_list = all_list_[index_no, :]
        file = str(all_list)
        gap = "_'"
        gap1 = " "
        for k in range(0,len(file)):
            if gap1 == file[k]:
                file = file.replace(gap1, '_')
        for k in range(0,6):
            file = file.replace("__'", " '")
            file = file.replace(gap, " '")
        tree_view.insert('',END,values=file)
    
    elif seah_name in name:
        # index_no = name.index(seah_name)
        # all_list = all_list_[index_no, :]
        # file = str(all_list)
        # gap = "_'"
        # gap1 = " "
        # for k in range(0,len(file)):
        #     if gap1 == file[k]:
        #         file = file.replace(gap1, '_')
        # for k in range(0,6):
        #     file = file.replace("__'", " '")
        #     file = file.replace(gap, " '")
        # tree_view.insert('',END,values=file)

        tick = 1
        for i,elem in enumerate(name):
            if seah_name == name[i]:
                file = str(all_list_[i, :])
                gap = "_'"
                gap1 = " "
                for k in range(0,len(file)):
                    if gap1 == file[k]:
                        file = file.replace(gap1, '_')
                for k in range(0,6):
                    file = file.replace("__'", " '")
                    file = file.replace(gap, " '")
                #  if tick == 1:
                #      lis = np.copy(ad)
                #      lis = str(lis)
                #      tick = 0
                #  else:
                #      lis = np.vstack((lis,ad))
                #      lis = str(lis)
                tree_view.insert('',END,values=file)

    else:
        messagebox.showerror(title="no data found", message="NO such Roll number or name found.")

    seah.destroy()

def search_student(master):
    global rollno_seah, name_seah, seah
    seah = Toplevel()
    seah.geometry("520x160+200+200")
    seah.grab_set()
    seah.resizable(False,False)
    seah.iconbitmap("setting\\assets\\icon.ico")
    seah.config(bg="black")
    label(seah, text="Enter Roll No.   :", x=10, y=10 )
    label(seah, text="Enter Full Name  :", x=10, y=60 )

    seah_rollno = StringVar()
    seah_name = StringVar()

    rollno_seah = Entry(seah, textvariable="", font=("times of India",15,'bold'),bd=5 )
    rollno_seah.place(x=260, y=10)

    name_seah = Entry(seah, textvariable="", font=("times of India",15,'bold'),bd=5 )
    name_seah.place(x=260, y=60)

    submit_b = Button(seah, text="Search", command=lambda : search_st(master=master), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=58, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",10,"bold"))
    submit_b.place(x=10,y=110)

    mainloop()


