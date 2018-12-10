class Validate:
    @classmethod
    def validate_errors(cls, field, value):
        result = []

        if field.type is int:
            pass

        elif field.type is str:
            if hasattr(field, 'max_length') and field.max_length:
                __length = field.max_length
                if len(value) > __length:
                    result.append({'max_length': f'Must be less or equal to {__length}'})

            if hasattr(field, 'min_length') and field.min_length:
                __length = field.min_length
                if len(value) < __length:
                    result.append({'min_length': f'Must be greater or equal to {__length}'})

        elif field.type in [list, tuple, dict]:
            if hasattr(field, 'max_element_count') and field.max_element_count:
                __length = field.max_element_count
                if len(value) > __length:
                    result.append({'max_element_count': f'Element count must be less or equal to {__length}'})

            if hasattr(field, 'min_element_count') and field.min_element_count:
                __length = field.min_element_count
                if len(value) < __length:
                    result.append({'min_element_count': f'Element count must be greater or equal to {__length}'})

        return result
