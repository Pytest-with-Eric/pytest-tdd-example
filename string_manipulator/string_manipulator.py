"""
Build a String Manipulator with the following requirements
- convert to lower case
- remove a defined pattern from the string
"""


class StringManipulator:
    def to_lower_case(self, my_string: str):
        if not my_string:
            return "String is empty"
        if not isinstance(my_string, str):
            return "Invalid input"
        return my_string.lower()

    def remove_pattern(self, my_string: str, pattern: str):
        if not my_string:
            return "String is empty"
        if pattern not in my_string:
            return "Pattern not found"
        if not isinstance(my_string, str):
            return "Invalid input"
        new_string = my_string.replace(pattern, "")
        return new_string