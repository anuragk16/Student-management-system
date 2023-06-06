from tkinter import messagebox
import pandas as pd
import numpy as np
from setting.load_and_save import *



def make_excel():
    all_list = np.load("DATA.npy")
    try:
        df = pd.DataFrame(all_list)
        filepath = 'STUDENTS_DATA.xlsx'
        df.to_excel(filepath, index=False)
        messagebox.showinfo(title="completed",message="Check the location where the program is located, Your file is saved.")

    except :
        messagebox.showerror(title="ERROR",message="First close the running excel file and then retry.")
