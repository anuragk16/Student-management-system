from tkinter import *
from tkinter import messagebox,Toplevel,simpledialog
from tkinter.ttk import Treeview
from setting.load_and_save import *
import numpy as np

def label(master, text="nothing", x=0, y=0):
    list_area = Label(master, text=text, bg="gray", font=("times of India",18,'bold'), fg="lightblue",)
    list_area.place(x=x, y=y)

def conform_update():

    def update_name():
        up_name = str(simpledialog.askstring(title="New name",prompt="Enter New Name :")).upper()
        all_list_[index_no,1] = up_name      # NAME
        np.save("DATA",all_list_)
        messagebox.showinfo(title="Name updated", message="Name is updated.")
        
    def update_mob():
        up_mob = str(simpledialog.askstring(title="New MOB",prompt="Enter New mobile No. :")).upper()
        all_list_[index_no,2] = up_mob      # mob
        np.save("DATA",all_list_)
        messagebox.showinfo(title="MOB updated", message="mobile No. is updated.")
        
    def update_dob():
        up_dob = str(simpledialog.askstring(title="New date of birth",prompt="Enter New date of birth :")).upper()
        all_list_[index_no,3] = up_dob      # dob
        np.save("DATA",all_list_)
        messagebox.showinfo(title="DOB updated", message="Date of birth is updated.")
        
    def update_gender():
        up_gender = str(simpledialog.askstring(title="gender",prompt="Enter Gender :")).upper()
        all_list_[index_no,4] = up_gender      # gender
        np.save("DATA",all_list_)
        messagebox.showinfo(title="DOB updated", message="Date of birth is updated.")
        
    def update_email():
        up_email = str(simpledialog.askstring(title="New email",prompt="Enter New Email :")).upper()
        all_list_[index_no,5] = up_email     # email
        np.save("DATA",all_list_)
        messagebox.showinfo(title="email updated", message="Email is updated.")
        
    def update_address():
        up_address = str(simpledialog.askstring(title="New address",prompt="Enter New Address :")).upper()
        all_list_[index_no,6] = up_address      # address
        np.save("DATA",all_list_)
        messagebox.showinfo(title="Address updated", message="Address is updated.")

    
        
    
    name_b = Button(head_, text="Update Name", command=lambda : update_name(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",14,"bold"))
    name_b.place(x=70,y=100)

    mob_b = Button(head_, text="Update mobile No.", command=lambda : update_mob(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",14,"bold"))
    mob_b.place(x=70,y=180)

    dob_b = Button(head_, text="Update DOB.", command=lambda : update_dob(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",14,"bold"))
    dob_b.place(x=350,y=100)

    gender_b = Button(head_, text="Update Gender", command=lambda : update_gender(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",14,"bold"))
    gender_b.place(x=350,y=180)

    email_b = Button(head_, text="Update Email", command=lambda : update_email(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",14,"bold"))
    email_b.place(x=630,y=100)

    address_b = Button(head_, text="Update Address", command=lambda : update_address(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",14,"bold"))
    address_b.place(x=630,y=180)

    done_b = Button(head_, text="Done", command=lambda : head_.destroy(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=10, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",14,"bold"))
    done_b.place(x=400,y=250)



def heading_click():
    global head_
    head_ = Toplevel()
    head_.geometry("1000x320+200+200")
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


    conform_b = Button(head_, text="Conform", command=lambda : conform_update(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=100, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",10,"bold"))
    conform_b.place(x=70,y=55)


def update_st():
    global index_no, all_list_
    try :
        update_rollno = int(rollno_update.get())
    except ValueError:
        messagebox.showerror(title="no roll no", message="Please type the roll no. correctly.")

    all_list_ = np.load("DATA.npy")

    rollno = list(all_list_[:,0])
    index_no = rollno.index(update_rollno)
    update.destroy()
    heading_click()



  
    

def update_student():
    global rollno_update, update
    update = Toplevel()
    update.geometry("520x110+200+200")
    update.grab_set()
    update.resizable(False,False)
    update.iconbitmap("setting\\assets\\icon.ico")
    update.config(bg="black")
    label(update, text="Enter Roll No. :", x=10, y=10 )

    rollno_update = Entry(update, textvariable="", font=("times of India",15,'bold'),bd=5 )
    rollno_update.place(x=260, y=10)

    submit_b = Button(update, text="Search", command=lambda : update_st(), bg="gray", relief= GROOVE, fg="skyblue", bd=5
                 ,highlightbackground="dimgray", width=58, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",10,"bold"))
    submit_b.place(x=10,y=60)
