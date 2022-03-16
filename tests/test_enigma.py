from enigma_one.enigma import Enigma
from enigma_one.rotors import ROTORS


def test_enigma():
    enigma = (
        Enigma()
        .add_rotor(ROTORS['I'], 1)
        .add_rotor(ROTORS['II'], 17)
        .add_rotor(ROTORS['III'], 12)
    )

    assert enigma.write('hello world') == 'kjtnq tipsw'
    assert enigma.write('kjtnq tipsw') == 'hello world'
