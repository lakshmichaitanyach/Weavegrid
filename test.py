import unittest
import json
import os
from application import app
from resources.browse import RootAPI, BrowseAPI

class BaseCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)
    def tearDown(self):
        pass

class TestRootApi(BaseCase):
    def test_successful_root_register(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        _payload = json.dumps({
            "root": dir_path
        })

        response = self.app.post('/', headers= {"Content-Type": "application/json"}, data=_payload)
        
        self.assertEqual(str, type(response.json["message"]), "test 1 failed")
        self.assertEqual("Root registered", response.json["message"], "test 2 failed")
        self.assertEqual(200, response.status_code, "test 3 failed")
        print("ROOT TEST CASES PASSED")
        print("================================================================================================================")
    
      
    def test_root_directory(self):

        dir_path = os.path.dirname(os.path.realpath(__file__))
        _payload = json.dumps({
            "root": dir_path
        })

        self.app.post('/', headers= {"Content-Type": "application/json"}, data=_payload)
        response = self.app.get('/')

        self.assertEqual(response.status_code, 200, "test 4 failed")
        print("ROOT DIRECTORY TESTS PASSED")
        print("================================================================================================================")

    
    def test_browseApi_response(self):
        '''
        '''
        dir_path = os.path.dirname(os.path.realpath(__file__))
        _payload = json.dumps({
            "root": dir_path
        })

        response_first = self.app.post('/', headers= {"Content-Type": "application/json"}, data=_payload)

        test_details = {
                "permissions": "-rw-rw-rw-",
                "size": 59,
                "uid": 0,
                "created At": "Wed Sep 22 08:47:49 2021"
            }
        test_response = { 
            "sample.txt": test_details
        }
        test_content = "This is Test Text File"

        #create test directory
        directory = "testdirectory"
        directory_path = os.path.join(dir_path, directory)
        if not os.path.exists("testdirectory"):
            os.mkdir(directory_path)

        file = "sampletest"
        file_path = os.path.join(directory_path, file+".txt")

        test_file = open(file_path, "w")
        test_text = "This is Test Text File"
        test_file.write(test_text)
        test_file.close()
        response_With_test = self.app.get('/')


        output = self.app.get('/?req_path=testdirectory/sampletest')
        response = output.get_data()
        self.assertEqual(200, output.status_code)
        print("LIST CONTENT TEST CASES")
        print("================================================================================================================")
        

if __name__ == "__main__":
    unittest.main()







