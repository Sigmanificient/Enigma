from enigma_one.rotor import Rotor as _Rotor


class _Component:
    def __init__(self, components):
        self.component = components

    def __getattribute__(self, item):
        return self.components[item]


Rotor = _Component(
    {
        'I': _Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
        'II': _Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
        'III': _Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'),
        'IV': _Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J'),
        'V': _Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')
    }
)
