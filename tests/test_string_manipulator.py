from string_manipulator.string_manipulator import StringManipulator


def test_convert_lower_case():
    sm = StringManipulator()
    res = sm.to_lower_case("PYTEST")
    assert res == "pytest"


def test_convert_lower_case_invalid_input():
    sm = StringManipulator()
    res = sm.to_lower_case(123)
    assert res == "Invalid input"
