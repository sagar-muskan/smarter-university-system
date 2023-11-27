import unittest
from datetime import datetime
from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        Trying to add a new quiz without a title.
        Code fails at 'app\\controllers\\quizzes_controller.py', line 63, in 'add_quiz'
        """
        # clear previous history of quizzes.
        self.ctrl.clear_data()
        # add a new quiz with empty title.
        quiz1_id = self.ctrl.add_quiz(None, "Sample Quiz 1", datetime.now(), datetime.now())
        # There should be a quiz though it is added without a title.
        # Expecting `quiz1_id` to be Not `None`.
        self.assertIsNotNone(quiz1_id, "The quiz is Not `None`")

    def test_expose_failure_02(self):
        """
        Test initializing the QuizzesController with an invalid file path and 
        performing standard operations to check error handling and data integrity.
        Code breaks at "app\\utils\\data_loader.py", line 20, in 'save_data'
        """
        invalid_file_path = "/invalid/path/quizzes.json"
        self.ctrl = QuizzesController(invalid_file_path)

        # Attempt to add a quiz and then retrieve it
        specific_datetime = datetime(2023, 11, 23, 12, 30, 0)  # Example datetime
        quiz_id = self.ctrl.add_quiz("Test Quiz", "This is a test quiz", specific_datetime, specific_datetime)
        
        # Attempt to retrieve the added quiz
        retrieved_quiz = self.ctrl.get_quiz_by_id(quiz_id)

        # Check if the quiz retrieval is handled properly
        self.assertIsNotNone(retrieved_quiz, "Retrieving a quiz should be handled properly even with an invalid file path")
    
    def test_expose_failure_03(self):
        """
        Trying to provide invalid utf-8 characters while creating a question.
        Code breaks at 'app\\utils\\utils.py', line 11, in 'generate_id'
        """
        # clear previous history of quizzes.
        self.ctrl.clear_data()
        # add a quiz
        quiz1_id = self.ctrl.add_quiz("Quiz1", "Sample Quiz 1", datetime.now(), datetime.now())
        # add a question to the quiz, but with invalid utf-8 character.
        question1_id = self.ctrl.add_question( quiz1_id, "Question 1 \ud800", "Sample Question1 1")
        # If invalid characters are provided, the question should not be added to the quiz and
        # `question1_id` should be `None`
        self.assertIsNone(question1_id, "The question is `None`")

    def test_expose_failure_04(self):
        """
        Trying to add a question with object as title.
        Here datetime object is passed as title.
        Code breaks at "app\\utils\\data_loader.py", line 21, in 'save_data'

        Note: Running this test case corrupts the `data\\quizzes_test.py` JSON structure. So, before re-running this
        or any of the previous test cases, please delete `data\\quizzes_test.py` file.
        """
        # clear previous history of quizzes.
        self.ctrl.clear_data()
        # add some quiz
        quiz1_id = self.ctrl.add_quiz("Quiz 1", "Sample Quiz 1", datetime.now(), datetime.now())
        # add a question to the quiz with `datetime` object as parameter
        question1_id = self.ctrl.add_question(quiz1_id, datetime.now(), datetime.now())
        # If invalid object is provided, the question should not be added to the quiz
        # `question1_id` should be `None`.
        self.assertIsNone(question1_id)


if __name__ == '__main__':
    unittest.main()