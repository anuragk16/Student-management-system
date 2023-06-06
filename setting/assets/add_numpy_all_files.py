import numpy as np

all_list = np.array([["R.No.","Name","Mob.","DOB.","Gender","Email","address"],
                      ['','','','','','','']],dtype=object)

np.save("DATA",all_list)
