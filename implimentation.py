from college import College
from department import Department
from student import Student
from subject import Subject
from utility import generate_student
import random


s1 = College(cid=101, cname= "DY patil", princi_name="patil", no_of_student=45)
# print(s1, "1111111111111111111111111111111111111111111111")
d1 = Department(did=123, dname="mechanical", hod="dr patil")
d2 = Department(did=134, dname="computer", hod="suryavanshi")
d3 = Department(did=145, dname="electronic", hod="bhoyer")
d4 = Department(did=156, dname= "civil",  hod="chavan")
# print(d1)
s1.Department.extend([d1, d2, d3, d4])
# print(s1)

studs = generate_student(45, Student)
# print(studs)


d1.students.extend(studs[0:9])
d2.students.extend(studs[9:18])
d3.students.extend(studs[18:35])
d4.students.extend(studs[35:46])
# print(d1)
# print(d4)
deps = [d1, d2, d3, d4]

for i in deps:
    i.no_of_student = len(i.students)

# print(d1)
# print(d3)
sub_list = ["math", "chemestry", "physics", "english", "engi drawing"]

sub1 = Subject(subid=111,subname= sub_list[0], is_practical= False)
sub2 = Subject(subid=222,subname= sub_list[1], is_practical= True)
sub3 = Subject(subid=333,subname= sub_list[2], is_practical= True)
sub4 = Subject(subid=444,subname= sub_list[3], is_practical= False)
sub5 = Subject(subid=555,subname= sub_list[4], is_practical= True)

list_subjects = [sub1, sub2, sub3, sub4, sub5]


random.shuffle(list_subjects)
    
for i in studs:
    random_sub = list_subjects[0:random.randint(1, 5)]    
    i.subjects.extend(random_sub)
    # print(i)
    
# print(s1.Department)

for dept in s1.Department:
    # print(f"-----------------------------{dept.departmentname}-----------------------------")
    for stud in dept.students:   
        # print(f"------------------------------{stud.studentname}------------------------------")
        # print(stud.studentage, "-----",stud.studentmarks)
        pass 


for dep in s1.Department:
    # print(dep.departmenthod, dep.deparmentid)
    for stud in dep.students:
        # print(stud.studentname, end="")
        pass
def get_stud_by_sub(enter):
    if type(enter) == str:
        for dep in s1.Department:
            for stud in dep.students:
                for sub in stud.subjects:
                    # if sub.subjectname == enter:
                    # print(sub.subjectname, "--------------str type------(one subject)")
                    pass
    else:
        for i in enter:
            for dep in s1.Department:
                for stud in dep.students:
                    for sub in stud.subjects:
                        # print(sub.subjectname, "-------------list type-------------(multiple sub in list)")
                        pass
            

# res = get_stud_by_sub(["mechanical", "computer"])    # to get multiple subsject in list (str objects (mechanical) becomes data type {list} if we put multiple elements in the list)
# res = get_stud_by_sub("mechanical")                  # to get single subject (list is not applicable on single object) so (mechanical) str still str data type


# def get_stud_by_sub(enter):
#     for dep in s1.Department:
#         if dep.departmentname == enter:
#             print(dep.students)

# res = get_stud_by_sub("mechanical")


def get_stud_by_sub(enter):
    mayh_student =[]
    for dept in s1.Department:      # department attributes
        for stud in dept.students:  # show student and sub
            l = list(map(lambda x: x.subjectname, stud.subjects)) 
            # print(l)
            if enter in l:
                mayh_student.append(stud)
                # print(mayh_student)
    # print(len(mayh_student))            

res = get_stud_by_sub("chemestry")                
            
            
for dep in s1.Department:
        # print(dep.students)
    lst = []
    for stud in dep.students:
        l = ((stud.studentname))
        # print(type(stud.studentname))
        lst.append(l)
    # print(lst)
        res = filter(lambda x: x[0] == "a", lst)
        print(list(res))

        



