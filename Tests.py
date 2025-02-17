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

# Example of bad practice usage
def main():
    obj = Final()
    test_data = [{"value": 5}, {"value": "HELLO"}, {"value": -2}, {"value": "hi"}, {}, {"other": 42}, {"value": None}]
    for data in test_data:
        print(obj.process(data))

if __name__ == "__main__":
    main()
