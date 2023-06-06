from tkinter import *
from tkinter import messagebox,Toplevel
from setting.load_and_save import *
import numpy as np
from tkinter.ttk import Treeview

def label(master, text="nothing", x=0, y=0):
    list_area = Label(master, text=text, bg="gray", font=("times of India",18,'bold'), fg="lightblue",)
    list_area.place(x=x, y=y)

def conform_delt():
    all_list_ = np.load("DATA.npy")
    all_list = np.delete(all_list_,index_no,0)
    np.save("DATA",all_list)
    messagebox.showinfo(title="DELETED", message="Student was deleted.")
    head_.destroy()

def heading_click():
    global head_
    head_ = Toplevel()
    head_.geometry("1000x100+200+200")
    head_.grab_set()
    head_.resizable(False,False)
    head_.iconbitmap("setting\\assets\\icon.ico")
    head_.config(bg="black")

    treev = Treeview(head_, selectmode ='browse')
    treev.place(x=0 , y=0 , width=1000 , height=50)
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
    rollno = list( all_list_[ :, 0])

    if delt_rollno in rollno and delt_rollno != "":
        index_no = rollno.index(delt_rollno)
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
        treev.insert('',END,values=file)

    conform_b = Button(head_, text="Conform", command=lambda : conform_delt(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=100, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",10,"bold"))
    conform_b.place(x=70,y=55)

def delete_st():
    global delt_rollno,index_no
    try :
        delt_rollno = int(rollno_delt.get())
    except ValueError:
        messagebox.showerror(title="no roll no", message="Please type the roll no. correctly.")

    all_list_ = np.load("DATA.npy")
    rollno = list( all_list_[ :, 0])

    if delt_rollno in rollno and delt_rollno != "":
        index_no = rollno.index(delt_rollno)
        messagebox.showwarning(title="WARNING", message="This process can not be undo.")
        heading_click()
    else:
        messagebox.showerror(title="no rollno found", message="NO Rollno found")

def delete_student():
    global rollno_delt, delt
    delt = Toplevel()
    delt.geometry("520x110+200+200")
    delt.grab_set()
    delt.resizable(False,False)
    delt.iconbitmap("setting\\assets\\icon.ico")
    delt.config(bg="black")
    label(delt, text="Enter Roll No.   :", x=10, y=10 )

    delt_rollno = StringVar()
    rollno_delt = Entry(delt, textvariable="", font=("times of India",15,'bold'),bd=5 )
    rollno_delt.place(x=260, y=10)

    submit_b = Button(delt, text="Search", command=lambda : delete_st(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=58, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",10,"bold"))
    submit_b.place(x=10,y=60)
