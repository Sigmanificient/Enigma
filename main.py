from string import ascii_uppercase


DEBUG = False


def debug(func):
    if not DEBUG:
        return func

    def wrapper(self, int_char):
        result = func(self, int_char)
        print(f'{self.__class__.__name__} -> {ascii_uppercase[result]}')
        return result

    return wrapper


class Rotor:

    def __init__(self, mapping):
        self.mapping = tuple(ascii_uppercase.index(char) for char in mapping)
        self.rotation = 0

    def rotate(self):
        self.rotation += 1
        self.rotation %= 26
        return self.rotation

    @debug
    def process(self, int_char):
        return self.mapping[(int_char + self.rotation) % 26]


ROTORS = {
    'IC': Rotor('DMTWSILRUYQNKFEJCAZBPGXOHV'),
    'IIC': Rotor('HQZGPJTMOBLNCIFDYAWVEUSRKX'),
    'IIIC': Rotor('UQNTLSZFMREHDPXKIBVYGJCWOA')
}


class Reflector:

    def __init__(self):
        self.mapping = tuple(ascii_uppercase.index(char) for char in 'QYHOGNECVPUZTFDJAXWMKISRBL')

    @debug
    def process(self, int_char):
        return self.mapping[int_char]


class Enigma:

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
        return (self.__handle_key(key.upper()) for key in keys)

    @staticmethod
    def __handle_plugboard(func):
        def inner(self, key):
            int_char = self.plugboard.get(key, key)
            r = func(self, int_char)
            return self.plugboard.get(r, r)

        return inner

    @__handle_plugboard
    def __handle_key(self, key):
        if key not in ascii_uppercase:
            return key

        if DEBUG:
            print('Processing key:', key)

        int_char = ascii_uppercase.index(key)

        for rotor in self.rotors:
            int_char = rotor.process(int_char)

        int_char = self.reflector.process(int_char)

        for rotor in reversed(self.rotors):
            int_char = rotor.process(int_char)

        return ascii_uppercase[int_char]


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
