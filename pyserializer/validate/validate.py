class Validate:
    @classmethod
    def validate_errors(cls, field, value):
        result = []
        if hasattr(field, 'max_length') and field.max_length:
            __length = field.max_length
            if len(value) > __length:
                result.append({'max_length': f'Must be less then {__length}'})

        if hasattr(field, 'min_length') and field.min_length:
            __length = field.min_length
            if len(value) < __length:
                result.append({'min_length': f'Must be greater then {__length}'})
        return result
