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


ROTORS = {
    'I': Rotor('JGDQOXUSCAMIFRVTPNEWKBLZYH', 'Q'),
    'II': Rotor('NTZPSFBOKMWRCJDIVLAEYUXHGQ', 'E'),
    'III': Rotor('JVIUBHTCDYAKEQZPOSGXNRMWFL', 'V'),
}
