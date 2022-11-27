import pytest

from odbm.models.validators import compare


@pytest.mark.parametrize(
    "validator_name, max_value, value",
    [
        ("validate_max_value", 10, 10),
        ("validate_min_value", 10, 10),
        ("validate_min_value", 10, float("inf")),
    ],
)
def test_builtin_types_valid(validator_name, max_value, value):
    validator = getattr(compare, validator_name)
    assert validator(max_value)(value) is None


@pytest.mark.parametrize(
    "validator_name, max_value, value, error_msg",
    [
        ("validate_max_value", 10, 11, "11 must be less than 10"),
        ("validate_min_value", 10, 9, "9 must be greater than 10"),
    ],
)
def test_builtin_types_invalid(validator_name, max_value, value, error_msg):
    validator = getattr(compare, validator_name)
    with pytest.raises(ValueError) as cm:
        validator(max_value)(value)
    assert str(cm.value) == error_msg
