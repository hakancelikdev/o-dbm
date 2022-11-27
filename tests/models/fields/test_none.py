from odbm.models.fields.none import NoneField
from odbm.models.validators import validate_none


def test_none_field_check_validator():
    field = NoneField()
    assert field.validators == [validate_none]
