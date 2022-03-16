from __future__ import annotations

from string import ascii_uppercase
from typing import Tuple, List, Callable, Dict

from enigma_one.components import Rotor, Reflector
from enigma_one.utils import DEBUG

Plugboard = Dict[str, str]


class Enigma:

    def __init__(self):
        self.rotors = []
        self.reflector = None
        self.plugboard = {}

    def add_rotor(self, rotor: Rotor, position: int) -> Enigma:
        rotor.rotation = position
        self.rotors.append(rotor)
        return self

    def set_reflector(self, reflector: Reflector) -> Enigma:
        self.reflector = reflector
        return self

    def set_plugboard(self, *swaps: Tuple[str, ...]) -> Enigma:
        for left, right in swaps:
            self.plugboard[left] = right
            self.plugboard[right] = left
        return self

    def run(self, keys: str) -> str:
        output_buffer: List[str] = []

        for key in keys:
            output_buffer.append(self.__handle_key(key.upper()))
            self.__rotate_rotors()

        return ''.join(output_buffer)

    def __rotate_rotors(self):
        state = 1

        for rotor in self.rotors:
            state = rotor.rotate(state)

    @staticmethod
    def __handle_plugboard(func) -> Callable[[Enigma, str], str]:
        def inner(self, key: str) -> str:
            int_char: int = self.plugboard.get(key, key)
            r: str = func(self, int_char)
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
