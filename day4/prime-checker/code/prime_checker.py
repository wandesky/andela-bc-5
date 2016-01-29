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


# class PrimeChecker(object):
#
#     def __init__(self, number=''):
#         self.number = number
#         if self.number == '':
#             self.number = 0
#         else:
#             self.number = int(self.number)
#
#     def is_prime(self):
#         if self.number < 2:
#             return False
#         else:
#             for i in range(2, self.number + 1):
#                 if i % 2 == 0:
#                     return True
#             return False
