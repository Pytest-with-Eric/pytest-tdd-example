from string_manipulator.string_manipulator import StringManipulator


def test_convert_lower_case():
    sm = StringManipulator()
    res = sm.to_lower_case("PYTEST")
    assert res == "pytest"
