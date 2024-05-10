class User:
    username = None
    password = None
    email = None
    IsActive = None
    projects = []

    def __init__(self , username , password , email , IsActive , projects):
        self.username = username
        self.password = password
        self.email = email
        self.IsActive = IsActive
        self,projects = projects

    