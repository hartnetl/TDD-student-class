import unittest
from student import Student


class TestStudent(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
