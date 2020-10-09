from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext, ugettext_lazy as _
from jsonschema import validate
from jsonschema.exceptions import ValidationError as JSONValidationError


class UsernameValidator(RegexValidator):
    regex = r"^[\w]+\Z"
    message = _(
        "Enter a valid username. This value may contain only letters, numbers, and _ character."
    )
    flags = 0


username_validators = [UsernameValidator()]


def JSONStringListValidator(value):
    TAGS_SCHEMA = {
        "type": "array",
        "items": {
            "type": "string",
            "minLength": 3,
            "maxLength": settings.MYAWESOMEAPP_TAG_LENGHT,
        },
    }
    try:
        validate(instance=value, schema=TAGS_SCHEMA)
    except JSONValidationError as e:
        raise ValidationError(e.message)
    except:
        raise ValidationError(_("Value must be valid JSON."))
