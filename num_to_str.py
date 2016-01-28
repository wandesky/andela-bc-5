in_words = "zero one two three four five six seven eight nine".split()


def num_to_str(number):
    lookup = dict(zip(range(10), in_words))
    return " ".join([lookup[int(char)] for char in str(number)])


def num_to_words(number):
    in_words = "zero one two three four five six seven eight nine".split()
    lookup = dict(zip(range(10), in_words))
    num_str = ''

    for char in str(number):
        if num_str:
            num_str += " " + lookup[int(char)]
        else:
            num_str += lookup[int(char)]
    return num_str


def num_to_words2(number):
    in_words = "zero one two three four five six seven eight nine".split()
    lookup = dict(zip(range(10), in_words))
    num_str = []
    for char in str(number):
        num_str.append(lookup[int(char)])
    return " ".join(num_str)


def num_to_str_v2(number):
    return " ".join([in_words[int(char)] for char in str(number)])


def num_to_str_another(number):
    in_words = "zero one two three four five six seven eight nine".split()
    number = str(number)
    num_string = ''
    lookup = {}
    index = 0
    for word in in_words:
        lookup[index] = word
        index += 1

    for char in number:
        if num_string:
            num_string += " " + lookup[int(char)]
        else:
            num_string += lookup[int(char)]

    return num_string


print(num_to_str(1234))
print(num_to_str_another(5678))
print(num_to_words(9101))
print(num_to_str_v2(1234))
