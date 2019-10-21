"""Unittests for leesbaarheidsindex.py"""

import unittest
import leesbaarheidsindex

class LeesbaarheidsindexTest(unittest.TestCase):

    def test_aantal_woorden(self):
        test_data = [
            ('een zin met vijf woorden', 5),
            ('een', 1),
            ('een zin met een komma, een . en uitroeptekens!!!!', 8),
        ]

        f = leesbaarheidsindex.aantal_woorden

        for s, expected in test_data:
            self.assertEqual(expected, f(s), s)

    def test_verwijder_leestekens(self):
        test_data = [
            ('.,:;?!&()[]{}', ''),
            ('Twee zinnen. met en!', 'Twee zinnen met en'),
        ]

        f = leesbaarheidsindex.verwijder_leestekens

        for s, expected in test_data:
            self.assertEqual(expected, f(s), s)

    def test_aantal_letters(self):
        test_data = [
            ('', 0),
            ('a', 1),
            ('abcde', 5),
        ]

        f = leesbaarheidsindex.aantal_letters

        for s, expected in test_data:
            self.assertEqual(expected, f(s), s)

    def test_aantal_lettergrepen(self):
        test_data = [
            ('een', 1),
            ('testen', 2),
            ('voorbeeld', 2),
            ('zeëen', 2),
            ('eieren', 3),
            ('leesbaarheid', 3),
        ]

        f = leesbaarheidsindex.aantal_lettergrepen

        for s, expected in test_data:
            self.assertEqual(expected, f(s), s)

    def test_aantal_zinnen(self):
        test_data = [
            ('een zin', 1),
            ('Eén zin!', 1),
            ('Twee zinnen? Tweede zin.', 2),
        ]

        f = leesbaarheidsindex.aantal_zinnen

        for s, expected in test_data:
            self.assertEqual(expected, f(s), s)

    def test_gemiddeld_aantal_woorden_per_zin(self):
        test_data = [
            ('Twee zinnen. Twee woorden!', 2),
            ('Een zin! Twee.', 1.5),
            ('Drie zinnen! Tweede. Derde met drie.', 2),
        ]

        f = leesbaarheidsindex.gemiddeld_aantal_woorden_per_zin

        for s, expected in test_data:
            self.assertEqual(expected, f(s), s)

    def test_gemiddelde_woordlengte(self):
        test_data = [
            ('een zin met aap kat', 3),
            ('twee drie vier vijf', 4),
            ('een twee', 3.5),
        ]

        f = leesbaarheidsindex.gemiddelde_woordlengte

        for s, expected in test_data:
            self.assertEqual(expected, f(s), s)

    def test_gemiddeld_aantal_lettergrepen_per_woord(self):
        test_data = [
            ('een zin', 1),
            ('lekker gek!', 1.5),
            ('lettergreep', 3),
        ]

        f = leesbaarheidsindex.gemiddeld_aantal_lettergrepen_per_woord

        for s, expected in test_data:
            self.assertEqual(expected, f(s), s)

    def test_leesbaarheidsindex(self):
        test_data = [
            ('een zin met aap noot mies', 124.26),
            ('een vreselijk ingewikkeld en gecompliceerd tekstfragment', -4.073333333333311),
        ]

        f = leesbaarheidsindex.leesbaarheidsindex

        for s, expected in test_data:
            self.assertAlmostEqual(expected, f(s), s)

    def test_flesch_douma_formule(self):
        # 206.84 - (0.77 * woordlengte) - (0.93 * zinslengte)
        test_data = [
            ((0, 0), 206.84),
            ((1, 0), 206.84 - 0.77 * 1),
            ((0, 1), 206.84 - 0.93 * 1),
        ]

        f = leesbaarheidsindex.flesch_douma_formule

        for args, expected in test_data:
            self.assertAlmostEqual(expected, f(*args), args)


if __name__ == '__main__':
    unittest.main()
