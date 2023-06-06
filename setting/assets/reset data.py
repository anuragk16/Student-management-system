import numpy as np

rollno = np.array(["Roll No."],dtype=object)

name = np.array(["Name"],dtype=object)

mob = np.array(["MOB"],dtype=object)

dob = np.array(["DOB"],dtype=object)

gender = np.array(["Gender"],dtype=object)

email = np.array(["Email"],dtype=object)

seahress = np.array(["seahress"],dtype=object)


all_list = np.hstack((rollno,name))
all_list = np.hstack((all_list,mob))
all_list = np.hstack((all_list,dob))
all_list = np.hstack((all_list,gender))
all_list = np.hstack((all_list,email))
all_list = np.hstack((all_list,seahress))

np.save("rollno",rollno)
np.save("name",name)
np.save("mob",mob)
np.save("dob",dob)
np.save("gender",gender)
np.save("email",email)
np.save("seahress",seahress)
np.save("all_list",all_list)
