# import time
from functools import wraps


def log(filename=None):
    """функция декоратор для логгирования выполнения функций"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = None
            if filename:
                file = open(filename, "a")
            name_function = str(func)[10 : str(func).find("0x") - 4]
            args_function = str(args) + "-" + str(kwargs)
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                #                print("\n ++мы попали в исключение \n")
                if filename:
                    #          file.write(f'{str(time.ctime())}: {name_function} error: {e} Inputs: {args_function}\n')
                    file.write(f"{name_function} error: {e} Inputs: {args_function}\n")
                else:
                    #              print(f'{str(time.ctime())}: {name_function} error: {e} Inputs: {args_function} \n')
                    print(f"{name_function} error: {e} Inputs: {args_function} \n")
            else:
                if filename:
                    #                    file.write(f'{str(time.ctime())} {name_function} OK \n')
                    file.write(f"{name_function} OK \n")
                else:
                    #                    print(f'{str(time.ctime())} {name_function} OK\n')
                    print(f"{name_function} OK\n")
            finally:
                if filename:
                    file.close()
            return result

        return inner

    return wrapper
