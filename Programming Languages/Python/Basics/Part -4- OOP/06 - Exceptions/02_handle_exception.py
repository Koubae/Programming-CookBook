class ConversionError(Exception):
    pass

def convert_int(val):
    if not isinstance(val, int):  # remember this will work for booleans too!
        raise TypeError()
    if val not in {0, 1}:
        raise ValueError("Integer values 0 or 1 only")
    return bool(val)

def convert_str(val):
    if not isinstance(val, str):
        raise TypeError()
        
    val = val.casefold()  # for case-insensitive comparisons
    if val in {'0', 'f', 'false'}:
        return False
    elif val in {'1', 't', 'true'}:
        return True
    else:
        raise ValueError('Admissible string values are: T, F, True, False (case insensitive)')
        
def make_bool(val):
    try:
        try:
            b = convert_int(val)
        except TypeError:
            # it wasn't an int/bool, so let's try it as a string
            try:
                b = convert_str(val)
            except TypeError:
                raise ConversionError(f'The type {type(val).__name__} cannot be converted to a bool')
    except ValueError as ex:
        # this will catch ValueError exceptions from either convert_int or convert_str
        raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}')
    else:
        return b



class ConversionError(Exception):
    pass

def convert_int(val):
    if not isinstance(val, int):  # remember this will work for booleans too!
        raise TypeError()
    if val not in {0, 1}:
        raise ValueError("Integer values 0 or 1 only")
    return bool(val)

def convert_str(val):
    if not isinstance(val, str):
        raise TypeError()
        
    val = val.casefold()  # for case-insensitive comparisons
    if val in {'0', 'f', 'false'}:
        return False
    elif val in {'1', 't', 'true'}:
        return True
    else:
        raise ValueError('Admissible string values are: T, F, True, False (case insensitive)')
        
def make_bool(val):
    try:
        try:
            b = convert_int(val)
        except TypeError:
            # it wasn't an int/bool, so let's try it as a string
            try:
                b = convert_str(val)
            except TypeError:
                raise ConversionError(f'The type {type(val).__name__} cannot be converted to a bool') from None
    except ValueError as ex:
        # this will catch ValueError exceptions from either convert_int or convert_str
        raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}') from None
    else:
        return b



try:
    raise ValueError('level 1')
except ValueError as ex_1:
    try:
        raise ValueError('level 2')
    except ValueError as ex_2:
        try:
            raise ValueError('level 3')
        except ValueError as ex_3:
            raise ValueError('value error occurred')



try:
    raise ValueError('level 1')
except ValueError as ex_1:
    try:
        raise ValueError('level 2')
    except ValueError as ex_2:
        try:
            raise ValueError('level 3')
        except ValueError as ex_3:
            raise ValueError('value error occurred') from None


try:
    raise ValueError('level 1')
except ValueError as ex_1:
    try:
        raise ValueError('level 2')
    except ValueError as ex_2:
        try:
            raise ValueError('level 3')
        except ValueError as ex_3:
            raise ValueError('value error occurred') from ex_1


def calc(b):
    try:
        b_bool = convert_int(b)
    except TypeError as ex_1:
        # bad type, but maybe it was a float and we could try to convert it to an int first
        try:
            b_int = int(b)
        except (ValueError, TypeError):
            raise CustomError('Bad type')
            
        b_bool = convert_int(b_int)

    return b_bool


def calc(b):
    try:
        b_bool = convert_int(b)
    except TypeError as ex_1:
        # bad type, but maybe it was a float and we could try to convert it to an int first
        try:
            b_int = int(b)
        except (ValueError, TypeError):
            raise CustomError('Bad type') from ex_1
            
        b_bool = convert_int(b_int)

    return b_bool