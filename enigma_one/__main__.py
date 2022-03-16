from enigma_one.enigma import Enigma
from enigma_one.rotors import ROTORS


def main():
    enigma = (
        Enigma()
            .add_rotor(ROTORS['I'], 6)
            .add_rotor(ROTORS['II'], 14)
            .add_rotor(ROTORS['III'], 2)
            .set_plugboard('bq', 'cr', 'di', 'ej', 'kw', 'mt', 'os', 'px', 'uz', 'gh')
    )

    print(''.join(enigma.write('Hello World')))


if __name__ == '__main__':
    main()
