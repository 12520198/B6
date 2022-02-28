from base_file import BaseClass

class Subject(BaseClass):
    def __init__(self, subid ,subname, is_practical):
        self.subject_id = subid
        self.subjectname = subname
        self.is_practical = is_practical



