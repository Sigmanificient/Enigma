from enigma_one.enigma import Enigma
from enigma_one.components import Rotor, Reflector


def test_enigma():
    enigma = (
        Enigma()
        .add_rotor(Rotor.I, 1)
        .add_rotor(Rotor.II, 17)
        .add_rotor(Rotor.III, 12)
        .set_reflector(Reflector.UKW_A)
        .set_plugboard('bq', 'cr', 'di', 'ej', 'kw', 'mt', 'os', 'px', 'uz', 'gh')
    )

    assert enigma.run('HELLO WORLD') == 'KJTNQ TIPSW'
    assert enigma.run('KJTNQ TIPSW') == 'HELLO WORLD'
