import unittest
from student import Student


class TestStudent(unittest.TestCase):
    # Test the full name
    def test_full_name(self):
        # We need to create an instance to test it
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")


if __name__ == "__main__":
    unittest.main()
