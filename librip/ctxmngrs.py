import time


class timer:
    def __enter__(self):
        begin_time = time.clock()

    def __exit__(self, type, value, traceback):
        print('Block has been executed during {:g} s'.format(time.clock()))
