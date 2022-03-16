from string import ascii_uppercase

from enigma_one.utils import debug


class Rotor:

    def __init__(self, mapping, turnover_char):
        self.mapping = tuple(ascii_uppercase.index(char) for char in mapping)
        self.rotation_point = ascii_uppercase.index(turnover_char)
        self.rotation = 0

    def rotate(self, previous_rotor):
        if not previous_rotor:
            return False

        self.rotation += 1
        self.rotation %= 26

        return self.rotation == self.rotation_point

    @debug
    def process(self, int_char):
        return self.mapping[(int_char + self.rotation) % 26]


ROTOR_I = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
ROTOR_II = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
ROTOR_III = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
ROTOR_IV = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J')
ROTOR_V = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')
