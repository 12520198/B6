import random

def get_random_name():
    w = ""
    for i in range(random.randint(4, 9)):
        s = chr(64 + random.randint(1, 26))
        w += s
    return w.title()
# print(get_random_name())




def generate_student(no, cls_nm):
    student_list = []
    for i in range(1, no+1):
        s = cls_nm(sid= 100+i, sname = get_random_name(), sage = random.randint(19, 26), smarks = random.randint(35, 100))
        student_list.append(s)
    return student_list
        
    






