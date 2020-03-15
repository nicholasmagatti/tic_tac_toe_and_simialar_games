from typing import Union


# Keep asking the user to insert an input until it is acceptable,
# then return the input as an int
def custom_int_input(message_before_input: str, acceptable_inputs: Union[list, range]):
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


def add_n_to_each_element(n, list_par: Union[list, range]):
    return list(map(lambda x: x + n, list_par))
