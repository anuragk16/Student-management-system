import numpy as np


temp_all_list = np.load
np.load = lambda *a,**k : temp_all_list(*a,allow_pickle=True,**k)

#["Roll No.","Name","Mob.","DOB.","Gender","Email","address"]
'''
all_list_splite = np.hsplit(all_list,7)



rollno = all_list_splite[0]
name = all_list_splite[1]
mob = all_list_splite[2]
dob = all_list_splite[3]
gender = all_list_splite[4]
email = all_list_splite[5]
address = all_list_splite[6]
'''