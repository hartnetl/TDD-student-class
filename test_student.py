import unittest
from student import Student


class TestStudent(unittest.TestCase):
    # Test the full name function
    def test_full_name(self):
        # We need to create an instance to test it
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")

    # Create test for changing naughty list to True
    def test_alert_santa(self):
        # Create instance
        student = Student("John",  "Doe")
        # Call the function
        student.alert_santa()
        # Check it changed
        self.assertTrue(student.naughty_list)


if __name__ == "__main__":
    unittest.main()
