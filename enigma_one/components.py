from enigma_one.reflector import Reflector as _Reflector
from enigma_one.rotor import Rotor as _Rotor


class _Component:
    def __init__(self, components):
        self.components = components

    def __getattribute__(self, item):
        return super().__getattribute__('components')[item]


Rotor = _Component(
    {
        'I': _Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
        'II': _Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
        'III': _Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'),
        'IV': _Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J'),
        'V': _Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')
    }
)

Reflector = _Component(
    {
        'UKW_A': _Reflector('EJMZALYXVBWFCRQUONTSPIKHGD'),
        'UKW_B': _Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT'),
        'UKW_C': _Reflector('FVPJIAOYEDRZXWGCTKUQSBNMHL')
    }
)
