#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first_name> <last_name>"

    :param first_name: First name (string)
    :param last_name: Last name (string, default="")
    :raises TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = f"My name is {first_name} {last_name}".strip()
    print(full_name)
