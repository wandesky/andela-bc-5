class StringSplosion(object):

    def __init__(self, string):
        self.string = string

    def manipulate(self):
        new_str = ''
        for i in range(len(self.string)):
            new_str += self.string[:i]

        new_str += self.string
        return new_str
