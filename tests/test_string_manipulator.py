from string_manipulator.string_manipulator import StringManipulator


def test_convert_lower_case():
    sm = StringManipulator()
    res = sm.to_lower_case("PYTEST")
    assert res == "pytest"


def test_convert_lower_case_input_type_int():
    sm = StringManipulator()
    res = sm.to_lower_case(123)
    assert res == "Invalid input"


def test_convert_lower_case_input_type_bool():
    sm = StringManipulator()
    res = sm.to_lower_case(True)
    assert res == "Invalid input"


def test_convert_lower_case_empty_string():
    sm = StringManipulator()
    res = sm.to_lower_case("")
    assert res == "String is empty"


def test_convert_lower_case_none_string():
    sm = StringManipulator()
    res = sm.to_lower_case(None)
    assert res == "String is empty"

def test_remove_pattern():
    sm = StringManipulator()
    res = sm.remove_pattern("Pytest with Eric", "Eric")
    assert res == "Pytest with "

def test_remove_pattern_empty_string():
    sm = StringManipulator()
    res = sm.remove_pattern("", "Eric")
    assert res == "String is empty"

def test_remove_pattern_none_string():
    sm = StringManipulator()
    res = sm.remove_pattern(None, "Eric")
    assert res == "String is empty"

def test_remove_pattern_doesnt_exist():
    sm = StringManipulator()
    res = sm.remove_pattern("Pytest with Eric", "John")
    assert res == "Pattern not found"