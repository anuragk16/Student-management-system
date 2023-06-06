from tkinter import *
from tkinter import messagebox
from main import Run


def label(master, text="nothing", x=0, y=0):
    list_area = Label(master, text=text, bg="gray", font=("times of India",18,'bold'), fg="lightblue",)
    list_area.place(x=x, y=y)

host_name = "anurag"
password = "anurag123"

def valid():
    Run()

def check_pass(master):
    host_input_name = (host_name_entry.get()).lower()
    password_input = password_entry.get()
    if host_input_name==host_name and password_input ==password:
        master.destroy()
        valid()
        

    elif host_input_name==host_name and password_input !=password:
        messagebox.showerror(title="Invalid password",message="Wrong Password !!")


    elif host_input_name!=host_name and password_input !=password:
        messagebox.showerror(title="Invalid password and username",message="Wrong Password and Host name !!")


    else: # host_input_name!=host_name and password_input ==password:
        messagebox.showerror(title="Invalid Host name",message="Wrong Host name !!")


log = Tk()
log.title("Student management system Login")
log.geometry("600x300+100+100")
log.minsize(600,300)
log.maxsize(600,300)
log.config(bg="black")
log.iconbitmap("setting\\assets\\icon.ico")

Label(log, text="Student management system Login", width=30, height=2, relief = RIDGE, borderwidth=2,
         fg="lightblue", bd=5, bg="gray", font=("Times of roman",25,"bold")).pack()

host_input_name = StringVar()
password_input = StringVar()

label(log, text="Enter Host Name  :", x=55, y=120 )
label(log, text="Enter Password   :", x=55, y=180 )

host_name_entry = Entry(log, textvariable=host_input_name, font=("times of India",15,'bold'),bd=5 )
host_name_entry.place(x=280, y=120)

password_entry = Entry(log, textvariable=password_input, font=("times of India",15,'bold'),bd=5 )
password_entry.place(x=280, y=180)

Button(log, text="SUBMIT", command= lambda : check_pass(log), bg="gray", relief= GROOVE, fg="skyblue", bd=8
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",15,"bold")).place(x=160,y=230)

mainloop()
