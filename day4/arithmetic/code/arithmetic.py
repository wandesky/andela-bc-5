def arith_geo(n):
    """Test whether a list is a Geometric progression, Arithmetic progression or neither."""
    def is_geometric(n):
        # Make sure you don't divide by zero
        if not n[0]:
            return False

        ratio = n[1] / n[0]
        for i in range(1, len(n) - 1):
            if not n[i]:  # If we have a zero somewhere in there, cannot be Geometric.
                return False
            elif ratio != n[i + 1] / n[i]:
                return False
        return True

    def is_arithmetic(n):
        d = n[1] - n[0]
        # Use list(range(n)) to convert into a list from a generator just in case we run on py3.
        return list(range(n[0], n[-1] + d, d)) == n

    if not n:
        return 0
    if len(n) <= 2:
        return -1

    elif is_geometric(n):
        return "Geometric"
    elif is_arithmetic(n):
        return "Arithmetic"

    return -1
