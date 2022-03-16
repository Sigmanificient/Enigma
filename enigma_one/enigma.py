from string import ascii_uppercase

from enigma_one.reflector import Reflector
from enigma_one.utils import DEBUG


class Enigma:

    def __init__(self):
        self.rotors = []
        self.reflector = None
        self.plugboard = {}

    def add_rotor(self, rotor, position):
        rotor.rotation = position
        self.rotors.append(rotor)
        return self

    def set_reflector(self, reflector):
        self.reflector = reflector
        return self

    def set_plugboard(self, *swaps):
        for left, right in swaps:
            self.plugboard[left] = right
            self.plugboard[right] = left
        return self

    def write(self, keys):
        output_buffer = []

        for key in keys:
            output_buffer.append(self.__handle_key(key.upper()))
            self.__rotate_rotors()

        return ''.join(output_buffer)

    def __rotate_rotors(self):
        state = 1

        for rotor in self.rotors:
            state = rotor.rotate(state)

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
