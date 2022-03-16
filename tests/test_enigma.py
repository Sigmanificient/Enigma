from enigma_one.enigma import Enigma
from enigma_one.rotors import ROTOR_I, ROTOR_II, ROTOR_III


def test_enigma():
    enigma = (
        Enigma()
        .add_rotor(ROTOR_I, 1)
        .add_rotor(ROTOR_II, 17)
        .add_rotor(ROTOR_III, 12)
        .set_plugboard('bq', 'cr', 'di', 'ej', 'kw', 'mt', 'os', 'px', 'uz', 'gh')
    )

    assert enigma.write('HELLO WORLD') == 'KJTNQ TIPSW'
    assert enigma.write('KJTNQ TIPSW') == 'HELLO WORLD'
