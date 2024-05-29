import unittest
import datetime
from tasks import Task
from projects import Projects
from user import User
from unittest.mock import patch
from comment import Commento
import json



class TestTask(unittest.TestCase) :
    
    @classmethod
    def setUpClass(cls):
        print("\nTASK ==========")
        
    
    def setUp(self) :
        self.task_1 = Task( "HIGH" , "MY_TASK_1" , "testing test in python 1" , "BACKLOG" )
        self.task_2 = Task( "LOW" , "MY_TASK_2" , "testing test in python 2" , "DONE" )
        
    def tearDown(self):
        pass
     
    def test_priority (self) :
        print("priority")
        self.assertEqual(self.task_1.priority , "HIGH")
        self.assertEqual(self.task_2.priority , "LOW")    
    
    def test_title (self) :
        print("title")
        self.assertEqual(self.task_1.title , "MY_TASK_1")
        self.assertEqual(self.task_2.title , "MY_TASK_2")    
    
    def test_discription (self) :
        print("discription")
        self.assertEqual(self.task_1.discription , "testing test in python 1")
        self.assertEqual(self.task_2.discription , "testing test in python 2")    
    
    def test_status (self) :
        print("status")
        self.assertEqual(self.task_1.status , "BACKLOG")
        self.assertEqual(self.task_2.status , "DONE")    

class TestProjects(unittest.TestCase) :
    
    @classmethod
    def setUpClass(cls):
        print("\nPROJECTS ==========")
       
    def setUp(self):
        self.project_1 = Projects("soroush" , "saleh")
        self.project_2 = Projects("saeed" , "soroush")
        self.user_1 = User("soroush" , "soroush@@2" , "soroush.faraz83@gmail.com" , True , [] )
        self.user_2 = User("saeed" , "saeed@@2" , "saeed.geshani84@gmail.com" , False , [] )
        
    def test_name (self) :
        print("name")
        self.assertEqual(self.project_1.name , "soroush")
        self.assertEqual(self.project_2.name , "saeed")
        
    def test_leader (self) :
        print("leader")
        self.assertEqual(self.project_1.leader , "saleh")
        self.assertEqual(self.project_2.leader , "soroush")
        
    def test_make_dict_of_project(self) :
        print("make_dict_of_project")
        self.assertEqual(self.project_1.make_dict_of_project() , {'ID': None, 'name': 'soroush', 'leader': 'saleh', 'members': [], 'tasks': []})
        self.assertEqual(self.project_2.make_dict_of_project() , {'ID': None, 'name': 'saeed', 'leader': 'soroush', 'members': [], 'tasks': []})

    "has some printing in it "
    @patch('builtins.input', side_effect=['My Project']) 
    def test_name_project (self , mock_input) :
        print("name_project")       
        
        self.project_1.name_project()
        self.assertEqual(self.project_1.name, 'My Project')

    @patch('builtins.input', side_effect=['*'])
    def test_name_project_cancel(self, mock_input):
        print("name_project")       
        self.project_1.name_project()
        self.assertEqual(self.project_1.name, "soroush")

    @patch('builtins.input', side_effect=['saleh', '*'])
    def test_add_member_existing(self, mock_input):
        # Test when the entered member name already exists
        In_account_user = self.user_1   # Replace with an actual user instance
        self.project_1.members_usernames = ['saleh']  # Existing members
        self.project_1.Add_member(In_account_user)
        self.assertEqual(self.project_1.members_usernames, ['saleh'])

    @patch('builtins.input', side_effect=['NewUser', 'saleh', '*'])
    def test_add_member_new(self, mock_input):

        In_account_user = self.user_1 
        self.project_1.members_usernames = ['saleh'] 
        self.project_1.Add_member(In_account_user)
        self.assertEqual(self.project_1.members_usernames, ['saleh'])

    @patch('builtins.input', side_effect=['*', 'saleh'])
    def test_add_member_cancel(self, mock_input):

        In_account_user = self.user_1  
        self.project_1.Add_member(In_account_user)
        self.assertEqual(self.project_1.members_usernames, [])

    @patch('builtins.input', side_effect=['123', '*'])
    def test_get_ID_unique(self, mock_input):       
        print("get_ID")         
        In_account_user = self.user_1  
        self.project_1.get_ID(In_account_user)
        self.assertEqual(self.project_1.ID, '123')

    @patch('builtins.input', side_effect=['456', '123', '*'])
    def test_get_ID_not_unique(self, mock_input):   
        print("get_ID")         
        In_account_user = self.user_1  
        self.project_1.ID = '456'
        self.project_1.get_ID(In_account_user)
        self.assertEqual(self.project_1.ID, '456')

        
    def test_save_my_project (self) :
        print("save_my_project")      
        user_1 = User("soroush" , "soroush@22" , "soroush.faraz83@gmail.com" , True , [])
        user_2 = User("ali" , "ali@22" , "ali.faraz83@gmail.com" , True , [])
            
        self.assertIsNone(self.project_1.save_my_project(user_1)) 
        self.assertIsNone(self.project_2.save_my_project(user_2))
         
    def test_finding_projects_leads (self) :
        print("finding_projects_leads")
        
        self.assertIsNone(self.project_1.finding_projects_leads()) 
        self.assertIsNone(self.project_1.finding_projects_leads())


class TestUser(unittest.TestCase) :
    
    @classmethod
    def setUpClass(cls):
        print("\nUSER ==========")
       
    def setUp(self):
        self.user_1 = User("soroush" , "soroush@@2" , "soroush.faraz83@gmail.com" , True , [] )
        self.user_2 = User("saeed" , "saeed@@2" , "saeed.geshani84@gmail.com" , False , [] )

    def test_name (self) :
        print("name")
        self.assertEqual(self.user_1.username , "soroush")
        self.assertEqual(self.user_2.username , "saeed")

    def test_password (self) :
        print("password")
        self.assertEqual(self.user_1.password , "soroush@@2")
        self.assertEqual(self.user_2.password , "saeed@@2")

    def test_email (self) :
        print("email")
        self.assertEqual(self.user_1.email , "soroush.faraz83@gmail.com")
        self.assertEqual(self.user_2.email , "saeed.geshani84@gmail.com")
        
    def test_IsActive (self) :
        print("IsActive")
        self.assertEqual(self.user_1.IsActive , True)
        self.assertEqual(self.user_2.IsActive , False)
                
    def test_projects (self) :
        print("projects")
        self.assertEqual(self.user_1.projects , [])
        self.assertEqual(self.user_2.projects , [])       
       
       
class TestCommento (unittest.TestCase) :
               
    @classmethod
    def setUpClass(cls):
        print("\nCOMMENT ==========")
       
    def setUp(self):
        self.comment_1 = Commento("soroush" , datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S") , "My comment-1")
        self.comment_2 = Commento("saeed" , datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S") , "My comment-2")

    def test_name (self) :
        print("name")
        self.assertEqual(self.comment_1.writer , "soroush")
        self.assertEqual(self.comment_2.writer , "saeed")

    def test_time (self) :
        print("time")
        self.assertEqual(self.comment_1.time ,  datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S") )
        self.assertEqual(self.comment_2.time ,  datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S") )              

    def test_text (self) :
        print("text")
        self.assertEqual(self.comment_1.text , "My comment-1")
        self.assertEqual(self.comment_2.text , "My comment-2")  
 
    def test_converting_to_str (self) :
        print("converting_to_str")
        self.assertEqual(self.comment_1.converting_to_dictionary() , {'Writer' : "soroush" , 'Text' : "My comment-1" , 'Time' : datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")})    
        self.assertEqual( self.comment_2.converting_to_dictionary() , {'Writer' : "saeed" , 'Text' : "My comment-2" , 'Time' : datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")})    
       
if __name__ == "__main__":
    unittest.main()
        
        
        