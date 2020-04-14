from typing import Union, Tuple, List


def custom_int_input(message_before_input: str, acceptable_inputs: Union[List[int], Tuple[int], range]) -> int:
    """
    Keeps asking the user to insert an input until it is acceptable,
    then return the input as an int.

    :param str message_before_input: message for user before asking for their input
    :param acceptable_inputs: acceptable inputs
    :type acceptable_inputs: Union[list, tuple, range]

    :return int: first acceptable input received from the user
    """
    acceptable = False
    # convert acceptable_inputs in strings
    [str(elem) for elem in acceptable_inputs]

    while not acceptable:
        try:
            input_received = int(input(message_before_input))
            if input_received in acceptable_inputs:
                acceptable = True
        except ValueError:
            pass  # so that it does not throw error, blocking the execution
        if not acceptable:
            print("Illegal input.")
    return input_received


def add_n_to_each_element(n: int, list_to_modify: Union[List[int], Tuple[int], range]) -> tuple:
    """
    Returns a tuple that is the inserted list/tuple/range with each
    number increased by the specified int.

    :param int n: number
    :param list_to_modify: list to add n to
    :type list_to_modify: Union[list, tuple, range]

    :return tuple: the inserted list/tuple/range with each
        number increased by the specified int
    """
    return tuple(map(lambda x: x + n, list_to_modify))
