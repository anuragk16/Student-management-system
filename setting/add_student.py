from tkinter import *
from tkinter import Toplevel,messagebox
import numpy as np
from setting.load_and_save import *

#["Roll No.","Name","Mob.","DOB.","Gender","Email","address"]

#########  LABEL FUNCTION FOR ALL LABELS
def label(master, text="nothing", x=0, y=0):
    list_area = Label(master, text=text, bg="gray", font=("times of India",18,'bold'), fg="lightblue",)
    list_area.place(x=x, y=y)

def give_rollno():
    global num
    all_list = np.load("DATA.npy")
    _list = np.hsplit(all_list,7)
    _list = _list[1]
    index_no = len(_list) -1
    if index_no == 1:
        num = 1
    else:
        num = all_list[index_no, 0] + 1
    return num
    
def submit_add():
    global all_list #,add_mob,add_dob,add_gender,add_email,add_address
    
    temp_all_list = np.load("DATA.npy")

    add_name = (name_entry.get()).upper()
    add_mob = (mob_entry.get()).upper()
    add_dob= (dob_entry.get()).upper()
    add_gender = (gender_entry.get()).upper()
    add_email = (email_entry.get()).upper()
    add_address = (address_entry.get()).upper()
    num = give_rollno()
    add_data = np.array([num,add_name,add_mob,add_dob,add_gender,add_email,add_address],dtype=object)
    all_list = np.vstack((temp_all_list,add_data))

    np.savez("DATA",all_list)
    np.save("DATA",all_list)

    messagebox.showinfo(title="SAVE SUCCESSFULL..",message="DATA SUCCESSFULLY SAVED>")
    add.destroy()
    return all_list
    
def add_student():
    global add,name_entry,mob_entry,dob_entry,gender_entry,email_entry,address_entry
    add = Toplevel()
    add.geometry("550x360+200+200")
    add.grab_set()
    add.resizable(False,False)
    add.iconbitmap("setting\\assets\\icon.ico")
    add.config(bg="black")

    ## name , mob , dob , address ,email, gender
    label(add, text="Enter Full Name  :", x=25, y=10 )
    label(add, text="Enter mobile No. :", x=25, y=60 )
    label(add, text="Enter Birth date :", x=25, y=110 )
    label(add, text="Enter Gender     :", x=25, y=160 )
    label(add, text="Enter Valid Email:", x=25, y=210 )
    label(add, text="Enter Address    :", x=25, y=260 )


    name_entry = Entry(add, textvariable="", font=("times of India",15,'bold'),bd=5 )
    name_entry.place(x=270, y=10)


    mob_entry = Entry(add, textvariable="+91-", font=("times of India",15,'bold'),bd=5 )
    mob_entry.place(x=270, y=60)
    mob_entry.setvar(name="+91-",value="+91-")

    dob_var = "dd | mm | yyyy"
    dob_entry = Entry(add, textvariable=dob_var, font=("times of India",15,'bold'),bd=5 )
    dob_entry.place(x=270, y=110)
    dob_entry.setvar(name="dd | mm | yyyy",value="dd | mm | yyyy")

    gender_var = "Male / Female"
    gender_entry = Entry(add, textvariable=gender_var, font=("times of India",15,'bold'),bd=5 )
    gender_entry.place(x=270, y=160)
    gender_entry.setvar(name="Male / Female", value="Male / Female")

    email_var = "@gmail.com"
    email_entry = Entry(add, textvariable=email_var, font=("times of India",15,'bold'),bd=5 )
    email_entry.place(x=270, y=210)
    email_entry.setvar(name="@gmail.com",value="@gmail.com")

    address_entry = Entry(add, textvariable="", font=("times of India",15,'bold'),bd=5 )
    address_entry.place(x=270, y=260)


    submit_b = Button(add, text="Submit", command=lambda : submit_add(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=58, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",10,"bold"))
    submit_b.place(x=25,y=310)

