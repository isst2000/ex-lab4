import random


def field(items, *args):
    assert len(args) > 0
    res = ""
    if len(args) == 1:
        for i in range(len(items)):
            if i != 0:
                res += ", "
            res += "'{}'".format(items[i][args[0]])
    else:
        for i in range(len(items)):
            if i != 0:
                res += ", "
            res += "{"
            f = 0
            for item in args:
                if f != 0:
                    res += ", "
                f += 1
                res += "'{}': '{}'".format(item, items[i][item])
            res += "}"
    print(res)


def gen_random(begin, end, num_count):
    res = [random.randrange(begin, end + 1) for i in range(num_count)]
    return res