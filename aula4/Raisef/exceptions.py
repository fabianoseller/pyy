class MyValueError(ValueError):
    """ Raise when a custom value error occurs."""

def divide_by_zero():
    return 1/0 # will fail and raise a ZeroDivisionError

try:
    raise MyValueError("My custom exception.")
    divide_by_zero()
except MyValueError as e:
    print(f"Caught custom value error: {repr(e)}")
except ValueError as e:
    print(f"Caught built-in value error: {repr(e)}")
