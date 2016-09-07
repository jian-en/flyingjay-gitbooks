def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


def normalize(numbers):
    total = sum(numbers)
    print total
    result = []
    for value in numbers:
        percent = 100.0 * value / total
        result.append(percent)
    return result


def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100.0 * value / total
        result.append(percent)
    return result


def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


class ReadVisits(object):

    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


if __name__ == '__main__':
    visits = ReadVisits('my_numbers.txt')
    it = iter(visits)
    print type(it)
    itt = iter(it)
    print iter(it) is iter(it)
