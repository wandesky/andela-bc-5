def super_sum(*args):
    """
    Sum up the arguments.

    Can sum up integer lists, sets, tuples or any nested combination of those.
    """
    def flatten(data_list, result=None):
        """Flatten any nested (list, set, tuple) and return a flat list."""
        if result is None:
            result = []
        for data in data_list:
            if isinstance(data, (list, tuple, set)):
                flatten(data, result)
            else:
                result.append(data)
        return result

    args = flatten(args)
    total = 0
    for arg in args:
        total += arg
    return total
