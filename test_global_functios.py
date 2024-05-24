from comment_and_member import Add_Comment
from comment_and_member import assigning_task_to_member
from in_project_workplace import *
from making_new_account import *
import unittest
import json


class TestAddComment(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\nADD_COMMENT ==============")
       

    def test_add_comment(self):

        ID = "c3beb888-12f8-4589-8421-6df7a01fce24"
        name = "pouria"
        comment_text = "This is a test comment."

        Add_Comment(ID, name)

        comment_text = "This is a test comment."

        with open("save_username_password_email.json", "r") as json_file:
            users_info = json.load(json_file)

        found_comment = True
        for user in users_info:
            for proj in user["projects_leads"]:
                for task in proj["tasks"]:
                    if ID == task["ID"]:
                        for comment in task["Comments"]:
                            if comment_text in comment:
                                found_comment = False
                                break

        self.assertTrue(found_comment, f"Comment didnt wrote for task ID: {ID}")

class TestAssigningTaskToMember(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\nASSIGNING_TASK_TO_MEMBER ==============")
    
    def test_assign_task_to_member(self):
        
        ID = "c3beb888-12f8-4589-8421-6df7a01fce24"
        assigning_task_to_member(ID)

        with open("save_username_password_email.json", "r") as json_file:
            users_info = json.load(json_file)

        found_task = False
        for user in users_info:
            for proj in user["projects_member"]:
                for task in proj["tasks"]:
                    if ID == task["ID"]:
                        found_task = True
                        break
        
        if found_task == False :
            print(f"Task hasnt been assigned for this member")
            self.assertFalse(found_task, f"Task hasnt been assigned for this member")
        if found_task :
            print(f"Task has been assigned for this member")
            self.assertTrue(found_task, f"Task has been assigned for this member")

# class Testshow_task(unittest.TestCase) :

#     @classmethod
#     def setUpClass(cls):
#         print("\nSHOW_TASK ==============")
    
#     def test_show_task(self) :
#         proj_path_leads = [0, 'projects_leads', 'tasks']
#         return_value = show_task(proj_path_leads)
        
#         self.assertEqual(return_value[0] ,{'Title': 'MY_F', 'Description': 'Just for testing this section of my code', 'Priority': 'CRITICAL', 'Status': 'DOING', 'Comments': [], 'ID': '8359ddfd-1b73-41fd-a2d2-557d46c0ee4a'})

class Testfinding_projects_leads(unittest.TestCase) :
    
    @classmethod
    def setUpClass(cls):
        print("\nFINDING_PROJECTS_LEADS ==============")
    
    def test_finding_projects_leads(self) :
        ID  = "1323"
        username = "saeed"
        return_value = finding_projects_leads(ID , username)
        self.assertEqual(return_value , [0, 'projects_leads', 'tasks'])

class Testfinding_projects_member(unittest.TestCase) :
    
    @classmethod
    def setUpClass(cls):
        print("\nFINDING_PROJECTS_MEMBER ==============")
    
    def test_finding_projects_member(self) :
        ID  = "1325"
        username = "soroush"
        return_value = finding_projects_member(ID , username)
        self.assertEqual(return_value , [2, 'projects_member', 'tasks'])

# class Testmy_validate_email(unittest.TestCase) :

#     @classmethod
#     def setUpClass(cls):
#         print("\nVALIDATE_EMAIL ==============")
    
#     def test_my_validate_email (self) :
#         default_email = "s.s@gmail.com"
#         my_emailaddress =  my_validate_email()
#         self.assertEqual(my_emailaddress , default_email)







if __name__ == "__main__":
    unittest.main()


