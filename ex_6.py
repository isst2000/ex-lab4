#!/usr/bin/env python3
import json
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random


path = 'data_light.json'
with open(path) as f:
    data = json.load(f)


# Helpful functions


def __prog(arr):
    if 'программист' in arr:
        return arr


def python(arr):
    return str(arr) + ' с опытом  Python'


@print_result
def f1(arg):
    return sorted(list(field(data, 'job-name')))


@print_result
def f2(arg):
    return list(filter(__prog, f1()))


@print_result
def f3(arg):
    return list(map(python, f2()))


@print_result
def f4(arg):
    return list(zip(f3(), gen_random(100000, 200000, len(f3()))))


with timer():
    f4(f3(f2(f1(data))))
