from base_file import BaseClass
# college - cid, cname, princi_name, no_of_studet
# department - did, dname, no_of student, hod
# student - sid sname, sage, smarks
# subject - subid, subname, is_practical

class College(BaseClass):
    def __init__ (self, cid, cname, princi_name, no_of_student):
        self.collegeid = cid
        self.college_name = cname
        self.principal  = princi_name
        self.college_stud = no_of_student
        self.Department = []

    

if __name__ == "__main__":

    s1 = College(cid=101, cname= "DY patil", princi_name="patil", no_of_student=45)
    print(s1)

