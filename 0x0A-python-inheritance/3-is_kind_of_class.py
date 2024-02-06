#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if it is an instance of a class that inherited from,
    the specified class.

    :param obj: The object to check.
    :param a_class: The class to compare against.
    :return: True if the object is an instance of, or if it is an instance of a class that inherited from,
             the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
