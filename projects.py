class Projects:
    ID = None
    name = None
    leader = None
    members = []
    tasks = []

    def __init__(self , name , leader):
        self.name = name
        self.leader = leader

    def make_dict_of_project(self):
        dicted_project = {'ID' : self.ID , 'name' : self.name , 'leader' : self.leader , 'members' : self.members , 'tasks' : self.tasks}
        return dicted_project

        