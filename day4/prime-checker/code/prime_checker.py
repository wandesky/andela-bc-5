class PrimeChecker1(object):

    def __init__(self, arg=''):
        self.arg = arg

    def is_prime(self):
        try:
            arg = int(self.arg)
        except (ValueError, TypeError):
            return False

        m = int(arg ** 0.5) + 1
        for i in range(2, m):
            if arg % i == 0:
                return False
        return True
