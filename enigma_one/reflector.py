from string import ascii_uppercase

from enigma_one.utils import debug


class Reflector:

    def __init__(self, mapping: str):
        self.mapping = tuple(ascii_uppercase.index(char) for char in mapping)

    @debug
    def process(self, int_char: int) -> int:
        return self.mapping[int_char]
