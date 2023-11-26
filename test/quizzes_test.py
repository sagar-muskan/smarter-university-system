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

if __name__ == '__main__':
    unittest.main()