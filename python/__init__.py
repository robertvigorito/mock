"""
Mock functions

Help test the deployment of the wgid pipeline, with this mock package
"""


def print_hello():
    """
    Print the message hello world.

    Returns:
        (str) String format of the message
    """
    message = "Hello World"
    print(message)
    return message


def print_with_args_kwargs(*arg, **kwargs):
    """
    print the arguments, for dictionary if they are provides,
    else pring noting and return False.

    Args:
        *arg (list):            List of arguments
        **kwargs (dict):        Key, value dictionary

    Returns:
        True if successful, False otherwise
    """
    if not all([arg, kwargs]):
        return False

    message = ""
    for a in arg:
        message += str(a) + "\n"

    for key, value in kwargs.items():
        message += f"{str(key)} - {str(value)}\n"

    print(message)
    return True


