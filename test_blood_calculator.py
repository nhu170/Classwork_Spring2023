# 1. Arrange
# 2. Act
# 3. Assert
# Test each one of the possible outcome, not only one
# Functions without input/output cannot be tested
# Functions that require user intervention cannot be tested either

# Having multiple assertions in one function is feasible
# But not the best pratice
# Use pytest.mark.parametrize as below

import pytest

# Can predefine the list


@pytest.mark.parametrize(
    "HDL_input, expected",
    [(65, "Normal"),
        (45, "Borderline Low"),
        (20, "Low")]
    )
def test_HDL_analysis(HDL_input, expected):
    from blood_calculator import HDL_analysis
    # Arrange
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == expected


@pytest.mark.parametrize(
    "LDL_input, expected",
    [(120, "Normal"),
        (135, "Borderline High"),
        (165, "High"),
        (200, "Very High")]
    )
def test_LDL_analysis(LDL_input, expected):
    from blood_calculator import LDL_analysis
    # Arrange
    # Act
    answer = LDL_analysis(LDL_input)
    # Assert
    assert answer == expected


def test_HDL_analysis_borderline_low():
    from blood_calculator import HDL_analysis
    # Arrange
    HDL_input_borderline_low = 45
    # Act
    answer = HDL_analysis(HDL_input_borderline_low)
    # Assert
    assert answer == "Borderline Low"
