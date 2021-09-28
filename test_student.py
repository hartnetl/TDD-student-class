import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    @classmethod
    # This acts on the class instead of the instance of a class
    def setUpClass(cls):
        print("Set up class")

    @classmethod
    def tearDownClass(cls):
        print("Tear dowm class")

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')

    # Test the full name function
    def test_full_name(self):
        print('test_full_name')
        # This tests each instance as it comes
        self.assertEqual(self.student.full_name, "John Doe")

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, "john.doe@email.com")

    # Create test for changing naughty list to True
    def test_alert_santa(self):
        print('test_alert_santa')
        # Call the function
        self.student.alert_santa()
        # Check it changed
        self.assertTrue(self.student.naughty_list)

    # Create test for extension
    def test_apply_extension(self):
        print("testing apply_extension")
        old_end_date = self.student.end_date
        # call function with parameter of 5 days
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    # Create successful call request
    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            # Set the values in student.py as if the test was successful
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")
            

     # Create failed call request
    def test_course_schedule_failed(self):
        """
        In the path "student" comes from the name of the file student.py
        """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")


if __name__ == "__main__":
    unittest.main()
