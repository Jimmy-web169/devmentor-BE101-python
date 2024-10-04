import unittest
from user import User, Student

class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User(id="A0001", email="jimmy@example.com", phone="0912345678", prefers_language="zh-TW")
        self.assertEqual(user.id, "A0001")
        self.assertEqual(user.email, "jimmy@example.com")
        self.assertEqual(user.phone, "0912345678")
        self.assertEqual(user.prefers_language, "zh-TW")

    def test_student_inherits_user(self):
        student = Student(id="A0001", email="jimmy@example.com", phone="0912345678", prefers_language="zh-TW")
        self.assertEqual(student.id, "A0001")
        self.assertEqual(student.email, "jimmy@example.com")
        self.assertEqual(student.phone, "0912345678")
        self.assertEqual(student.prefers_language, "zh-TW")

if __name__ == '__main__':
    unittest.main()