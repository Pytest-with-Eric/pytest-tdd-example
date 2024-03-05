"""
Build a String Manipulator with the following requirements
- convert to lower case
- convert to upper case
- reverse the string
- remove a defined pattern from the string
- find a defined substring
- remove whitespaces from the string
- make sure the string is not empty
- capitalize the first letter
- capitalize the first letter of every word
- check if the string is a palindrome or not
"""


class StringManipulator:
    def to_lower_case(self, my_string: str):
        if not my_string:
            return "String is empty"
        if not isinstance(my_string, str):
            return "Invalid input"
        return my_string.lower()

    def remove_pattern(self, my_string: str, pattern: str):
        if pattern not in my_string:
            return "Pattern not found"
        if not my_string:
            return "String is empty"
        if not isinstance(my_string, str):
            return "Invalid input"
        new_string = my_string.replace(pattern, "")
        return new_string
