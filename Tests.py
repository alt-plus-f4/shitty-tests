import unittest

class Base:
    def process(self, data):
        if self._is_valid_dict(data):
            return self._process_value(data.get('value'))
        return "INVALID DATA"

    def _is_valid_dict(self, data):
        return isinstance(data, dict)

    def _process_value(self, value):
        if isinstance(value, int):
            return self._process_int(value)
        elif isinstance(value, str):
            return self._process_str(value)
        return "UNKNOWN VALUE TYPE"

    def _process_int(self, value):
        if value > 0:
            return self._process_positive_int(value)
        elif value == 0:
            return "ZERO"
        return "NEGATIVE NUMBER"

    def _process_positive_int(self, value):
        if value % 2 == 0:
            return "POSITIVE EVEN NUMBER"
        return "POSITIVE ODD NUMBER"

    def _process_str(self, value):
        if value:
            if len(value) > 5:
                return self._process_long_string(value)
            return self._process_short_string(value)
        return "EMPTY STRING"

    def _process_long_string(self, value):
        if value.isupper():
            return "LONG UPPERCASE STRING"
        return "LONG STRING"

    def _process_short_string(self, value):
        if value.islower():
            return "SHORT LOWERCASE STRING"
        return "SHORT STRING"

class Intermediate(Base):
    def process(self, data):
        result = super().process(data)
        return self._process_result(result)

    def _process_result(self, result):
        if isinstance(result, str):
            if "ERROR" in result:
                return self._process_error(result)
            return self._categorize_result(result)
        return "UNHANDLED RESULT TYPE"

    def _process_error(self, result):
        if "MISSING" in result:
            return "CRITICAL ERROR: VALUE MISSING"
        elif "INVALID" in result:
            return "CRITICAL ERROR: DATA INVALID"
        return "UNKNOWN CRITICAL ERROR"

    def _categorize_result(self, result):
        if "NUMBER" in result:
            return self._categorize_number(result)
        elif "STRING" in result:
            return self._categorize_string(result)
        return "UNKNOWN CATEGORY"

    def _categorize_number(self, result):
        if "EVEN" in result:
            return "CONFIRMED EVEN"
        elif "ODD" in result:
            return "CONFIRMED ODD"
        elif "ZERO" in result:
            return "CONFIRMED ZERO"
        return "UNEXPECTED NUMBER CASE"

    def _categorize_string(self, result):
        if "LONG" in result:
            return "LONG CONFIRMED STRING"
        elif "SHORT" in result:
            return "SHORT CONFIRMED STRING"
        return "GENERAL CONFIRMED STRING"

class Final(Intermediate):
    def process(self, data):
        result = super().process(data)
        return self._final_check(result)

    def _final_check(self, result):
        if isinstance(result, str):
            if "CONFIRMED" in result:
                return self._confirm_result(result)
            return "FINAL CHECK: UNCATEGORIZED RESULT"
        return "FINAL CHECK: UNHANDLED RESULT TYPE"

    def _confirm_result(self, result):
        if "EVEN" in result:
            return "FINAL CHECK: EVEN NUMBER"
        elif "ODD" in result:
            return "FINAL CHECK: ODD NUMBER"
        elif "STRING" in result:
            return "FINAL CHECK: STRING"
        return "FINAL CHECK: UNEXPECTED CONFIRMATION"

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


def main():
    obj = TestProcessing()
    obj.setUp()
    obj.test_base_methods()
    obj.test_intermediate_methods()
    obj.test_final_methods()

if __name__ == "__main__":
    main()
