import unittest
from temp01 import check_password_strength

class TestPasswordStrength(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(check_password_strength(''), '弱')
    def test_short(self):
        self.assertEqual(check_password_strength('abc'), '弱')
    def test_only_lower(self):
        self.assertEqual(check_password_strength('abcdefgh'), '中')
    def test_only_upper(self):
        self.assertEqual(check_password_strength('ABCDEFGH'), '中')
    def test_only_digits(self):
        self.assertEqual(check_password_strength('12345678'), '中')
    def test_only_special(self):
        self.assertEqual(check_password_strength('!@#$%^&*'), '中')
    def test_mixed_medium(self):
        self.assertEqual(check_password_strength('Abcdef12'), '中')
    def test_strong(self):
        self.assertEqual(check_password_strength('Abc123!@'), '強')
    def test_strong2(self):
        self.assertEqual(check_password_strength('Password123!'), '強')

if __name__ == '__main__':
    unittest.main()
