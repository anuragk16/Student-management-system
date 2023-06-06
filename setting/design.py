from time import strftime
from tkinter import *
from setting.add_student import *
from setting.delete_student import *
from setting.update_student import *
from setting.search_student import *
from setting.Make_Excel_File import make_excel
from setting.show_all import *


def show_time():
    current_date = strftime("%d / %b / %Y")
    current_time = strftime("%I : %M %p")
    full_datetime = f"Time: {current_time} \nDate: {current_date}"
    datetime_label = Label(win, text=full_datetime, width=20, height=3, relief = RIDGE, borderwidth=2,
                      fg="lightblue", bd=5, bg="gray", font=("Times of roman",14,"bold") )
    datetime_label.place(x=950,y=5)
    datetime_label.after(200,show_time)

def Run_design():
    global win
    win = Tk()
    win.title("Student management system")
    win.geometry("1200x600+100+100")
    win.minsize(1200,600)
    win.maxsize(1200,600)
    win.config(bg="black")
    win.iconbitmap("setting\\assets\\icon.ico")

    Label(win, text="Student management system", width=25, height=2, relief = RIDGE, borderwidth=2,
         fg="lightblue", bd=5, bg="gray", font=("Times of roman",25,"bold")).pack()

    ####################### FRAMES AND DATETIME
    
    buttons_frame = Frame(win, bg="gray10", relief= GROOVE , borderwidth=2)
    buttons_frame.place(x=100 , y=120 , width=1000 , height=200)
    show_time()

    
    list_frame = Frame(win, bg="gray10", relief= GROOVE , borderwidth=2)
    list_frame.place(x=100 , y=350 , width=1000 , height=220)

    

    ####################### BUTTONS

    Button(win, text="add Student", command= lambda : add_student(), bg="gray", relief= GROOVE, fg="skyblue", bd=8
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",15,"bold")).place(x=140,y=140)

    Button(win, text="Search Student", command= lambda : search_student(win), bg="gray", relief= GROOVE, fg="skyblue", bd=8
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",13,"bold")).place(x=500,y=130)

    Button(win, text="Delete Student", command= lambda : delete_student(), bg="gray", relief= GROOVE, fg="skyblue", bd=8
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",15,"bold")).place(x=800,y=140)

    Button(win, text="Update Student", command= lambda : update_student(), bg="gray", relief= GROOVE, fg="skyblue", bd=8
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",15,"bold")).place(x=140,y=230)

    Button(win, text="Show All", command= lambda : show_all(win), bg="gray", relief= GROOVE, fg="skyblue", bd=8
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",13,"bold")).place(x=500,y=193)

    Button(win, text="Make Excel File", command= lambda : make_excel(), bg="gray", relief= GROOVE, fg="skyblue", bd=8
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",15,"bold")).place(x=800,y=230)

    Button(win, text="Exit", command= lambda : win.destroy(), bg="gray", relief= GROOVE, fg="skyblue", bd=8
                 ,highlightbackground="dimgray", width=20, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",12,"bold")).place(x=500,y=255)
    
    ################################ Treeview [list]


    
    treeviewshow(win)
     
    

    mainloop()

