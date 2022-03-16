from string import ascii_uppercase

from enigma_one.utils import debug


class Reflector:

    def __init__(self, sequence):
        self.mapping = tuple(ascii_uppercase.index(char) for char in sequence)

    @debug
    def process(self, int_char):
        return self.mapping[int_char]
