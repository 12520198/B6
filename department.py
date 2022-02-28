from base_file import BaseClass

class Department(BaseClass):
    def __init__ (self, did, dname, hod):
        self.deparmentid = did
        self.departmentname = dname
        self.departmenthod = hod
        self.no_of_student = None
        self.students = []
        
        

        
