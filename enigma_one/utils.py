from string import ascii_uppercase

DEBUG = True


def debug(func):
    if not DEBUG:
        return func

    def wrapper(self, int_char: int) -> int:
        result: int = func(self, int_char)
        print(f'{self.__class__.__name__} -> {ascii_uppercase[result]}')
        return result

    return wrapper
