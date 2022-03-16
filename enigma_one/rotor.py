from string import ascii_uppercase

from enigma_one.utils import debug


class Rotor:

    def __init__(self, mapping: str, turnover_char: str):
        self.mapping = tuple(ascii_uppercase.index(char) for char in mapping)
        self.rotation_point = ascii_uppercase.index(turnover_char)
        self.rotation = 0

    def rotate(self, previous_rot: bool) -> bool:
        if not previous_rot:
            return False

        self.rotation += 1
        self.rotation %= 26

        return self.rotation == self.rotation_point

    @debug
    def process(self, int_char: int) -> int:
        return self.mapping[(int_char + self.rotation) % 26]
