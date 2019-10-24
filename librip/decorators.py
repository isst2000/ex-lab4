def print_result(any_func):
    def wrapper():
        print(any_func.__name__)
        res = any_func()
        if isinstance(res, list):
            for i in range(len(res)):
                print(res[i])
        elif isinstance(res, dict):
            for k in res:
                print('{} = {}'.format(k, res[k]))
        else:
            print(any_func())
    return wrapper()