import unittest
from tasks import Task

class TestTask(unittest.TestCase) :
    
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

       
if __name__ == "__main__":
    unittest.main()
        
        
        