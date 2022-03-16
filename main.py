class Rotor:

    def __init__(self, mapping):
        self.mapping = mapping
        self.rotation = 0

    def rotate(self):
        self.rotation += 1
        self.rotation %= 26
        return self.rotation

    def process(self, int_char):
        return self.mapping[(int_char + self.rotation) % 26]


ROTORS = {
    'IC': Rotor('DMTWSILRUYQNKFEJCAZBPGXOHV'),
    'IIC': Rotor('HQZGPJTMOBLNCIFDYAWVEUSRKX'),
    'IIIC': Rotor('UQNTLSZFMREHDPXKIBVYGJCWOA')
}


class Reflector:

    def __init__(self):
        self.mapping = []

    def process(self, int_char):
        return self.mapping[int_char]


class Enigma:
    charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self.rotors = []
        self.reflector = Reflector()
        self.plugboard = {}

    def add_rotor(self, rotor):
        self.rotors.append(rotor)
        return self

    def set_plugboard(self, *swaps):
        for left, right in swaps:
            self.plugboard[left] = right
            self.plugboard[right] = left
        return self

    def write(self, keys):
        return (self.__handle_key(key) for key in keys)

    @staticmethod
    def __handle_plugboard(func):
        def inner(self, key):
            int_char = self.plugboard.get(key, key)
            r = func(self, int_char)
            return self.plugboard.get(r, r)
        return inner

    @__handle_plugboard
    def __handle_key(self, key):
        key = key.upper()

        if key not in self.charset:
            return key

        int_char = self.charset.index(key)

        int_char += 10
        int_char %= 26

        return self.charset[int_char]


def main():
    enigma = (
        Enigma()
        .add_rotor(ROTORS['IC'])
        .add_rotor(ROTORS['IIC'])
        .add_rotor(ROTORS['IIIC'])
        .set_plugboard('AB', 'ON', 'QR', 'ZY')
    )

    print(''.join(enigma.write('Hello World')))


if __name__ == '__main__':
    main()
