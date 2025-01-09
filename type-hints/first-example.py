# type hints in python
# this is a comment

def returning_string(name : str) -> str:
    """
    This function takes a string as an argument and returns a string
    
    """
    string_to_return = f"Hello {name}"
    return string_to_return

# get the return value, or string
returned_string = returning_string("John")
print(returned_string)