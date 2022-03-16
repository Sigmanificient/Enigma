from enigma_one.enigma import Enigma


def test_plugboard():
    swaps = ('bq', 'cr', 'di', 'ej', 'kw', 'mt', 'os', 'px', 'uz', 'gh')

    enigma = Enigma()
    enigma.set_plugboard(*swaps)

    for (l, r) in swaps:
        assert enigma.plugboard.get(l) == r
        assert enigma.plugboard.get(r) == l
