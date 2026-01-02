import unittest
from MyBigNumber import MyBigNumber

class TestMyBigNumber(unittest.TestCase):
    def test_sum_standard(self):
        obj = MyBigNumber()
        # Kiểm tra ví dụ 1234 + 897 = 2131 [cite: 16]
        self.assertEqual(obj.sum("1234", "897"), "2131")

    def test_sum_with_carry(self):
        obj = MyBigNumber()
        self.assertEqual(obj.sum("99", "1"), "100")

if __name__ == '__main__':
    unittest.main()