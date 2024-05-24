from comment_and_member import Add_Comment
from comment_and_member import assigning_task_to_member
import unittest
import json


class TestAddComment(unittest.TestCase):
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





if __name__ == "__main__":
    unittest.main()


