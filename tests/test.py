import unittest
from src.Tests import Base
from src.Tests import Intermediate
from src.Tests import Final

class TestProcessing(unittest.TestCase):
    def setUp(self):
        self.base = Base()
        self.intermediate = Intermediate()
        self.final = Final()

    def test_base_methods(self):
        self.assertEqual(self.base._is_valid_dict({}), True)
        self.assertEqual(self.base._is_valid_dict([]), False)
        self.assertEqual(self.base._process_int(5), "POSITIVE ODD NUMBER")
        self.assertEqual(self.base._process_int(4), "POSITIVE EVEN NUMBER")
        self.assertEqual(self.base._process_int(-1), "NEGATIVE NUMBER")
        self.assertEqual(self.base._process_int(0), "ZERO")
        self.assertEqual(self.base._process_str("HELLO"), "SHORT STRING")
        self.assertEqual(self.base._process_str("HELLOWORLD"), "LONG UPPERCASE STRING")
        self.assertEqual(self.base._process_str(""), "EMPTY STRING")
        self.assertEqual(self.base._process_str("HELLO WORLD"), "LONG UPPERCASE STRING")
        self.assertEqual(self.base._process_str("hello"), "SHORT LOWERCASE STRING")
        self.assertEqual(self.base._process_str("Hello"), "SHORT STRING")

    def test_intermediate_methods(self):
        self.assertEqual(self.intermediate._categorize_number("POSITIVE EVEN NUMBER"), "CONFIRMED EVEN")
        self.assertEqual(self.intermediate._categorize_number("POSITIVE ODD NUMBER"), "CONFIRMED ODD")
        self.assertEqual(self.intermediate._categorize_number("ZERO"), "CONFIRMED ZERO")
        self.assertEqual(self.intermediate._categorize_string("LONG STRING"), "LONG CONFIRMED STRING")
        self.assertEqual(self.intermediate._categorize_string("SHORT STRING"), "SHORT CONFIRMED STRING")
        self.assertEqual(self.intermediate._categorize_string("UNKNOWN"), "GENERAL CONFIRMED STRING")

    def test_final_methods(self):
        self.assertEqual(self.final._confirm_result("CONFIRMED EVEN"), "FINAL CHECK: EVEN NUMBER")
        self.assertEqual(self.final._confirm_result("CONFIRMED ODD"), "FINAL CHECK: ODD NUMBER")
        self.assertEqual(self.final._confirm_result("LONG CONFIRMED STRING"), "FINAL CHECK: STRING")
        self.assertEqual(self.final._confirm_result("SHORT CONFIRMED STRING"), "FINAL CHECK: STRING")
        self.assertEqual(self.final._confirm_result("GENERAL CONFIRMED STRING"), "FINAL CHECK: STRING")
        self.assertEqual(self.final._confirm_result("UNKNOWN"), "FINAL CHECK: UNEXPECTED CONFIRMATION")

if __name__ == "__main__":
    unittest.main()
