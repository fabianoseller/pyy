def divide_by_zero():
    return 1/0 # will fail and raise a ZeroDivisionError

try:
    divide_by_zero()
    raise Exception("My custom exception.")
except ValueError as e:
    print(f"Caught value error: {repr(e)}")
except Exception as e:
    print(f"Caught custom exception: {repr(e)}")
