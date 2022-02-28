from base_file import BaseClass

class Student(BaseClass):
    def __init__(self, sid, sname, sage, smarks):
        self.studentid = sid
        self.studentname = sname
        self.studentage = sage
        self.studentmarks = smarks
        self.subjects = []
