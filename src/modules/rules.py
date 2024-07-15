import datetime


def execute_callbacks(callbacks, days_to_execute, *args, **kwargs):
    """
    Executes the callbacks recursively if the current day is in the list of days to execute.

    Args:
        callbacks (list): List of callback functions to execute.
        days_to_execute (list): List of days to execute callbacks on.

    Returns:
        The result of the last callback if the current day is in the list of days to execute.
        None otherwise.
    """
    current_date = datetime.date.today()
    if current_date.weekday() in days_to_execute:
        if callbacks:
            result = callbacks[0](*args, **kwargs)
            return execute_callbacks(callbacks[1:], days_to_execute, result)
        else:
            return None


if __name__ == '__main__':
    def callback_example_1(param1, param2):
        print("Executing callback 1 with params", param1, param2)
        return param1 + param2

    def callback_example_2(result):
        print("Executing callback 2 with result", result)
        return result * 2

    callbacks_to_execute = [callback_example_1, callback_example_2]
    days_to_execute = [0, 1, 2, 3, 4, 5, 6]

    result = execute_callbacks(callbacks_to_execute, days_to_execute, "param1", "param2")
    if result is not None:
        print("Final result:", result)
    else:
        print("Callbacks not executed.")




