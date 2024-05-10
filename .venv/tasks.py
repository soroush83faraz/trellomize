class Task:
    ID = None
    title = None
    discription = None
    start_date = None
    end_date = None
    assignees = None
    priority = None
    status = None
    comments = {}
    history = None

    def __init__(self , ID , title , discription , start_date , end_date , assignees , priority , status):
        self.ID = ID
        self.title = title
        self.discription = discription
        self.start_date = start_date
        self.end_date = end_date
        self.assignees = assignees
        self.priority = priority
        self.status = status

