class Validate:
    @classmethod
    def validate_errors(cls, field, value):
        result = []

        if field.type is int:
            pass

        elif field.type in [str, list, tuple, dict]:
            if hasattr(field, 'max_length') and field.max_length:
                __length = field.max_length
                if len(value) > __length:
                    result.append({'max_length': f'Length must be less or equal to {__length}'})

            if hasattr(field, 'min_length') and field.min_length:
                __length = field.min_length
                if len(value) < __length:
                    result.append({'min_length': f'Length must be greater or equal to {__length}'})
        return result
