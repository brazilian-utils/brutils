import unittest

from datetime import datetime
from brutils.legal_process import (
    format_processo_juridico,
    remove_symbols,
    generate_processo_juridico,
    _checksum,
    is_valid_processo_juridico,
)


class TestLegalProcess(unittest.TestCase):
    def test_format_processo_juridico(self):
        self.assertEqual(
            format_processo_juridico("23141945820055070079"),
            ("2314194-58.2005.5.07.0079"),
        )
        self.assertEqual(
            format_processo_juridico("00000000000000000000"),
            ("0000000-00.0000.0.00.0000"),
        )
        self.assertIsNone(format_processo_juridico("2314194582005507"))
        self.assertIsNone(format_processo_juridico("0000000000000000000000000"))
        self.assertIsNone(format_processo_juridico("0000000000000000000asdasd"))

    def test_remove_symbols(self):
        self.assertEqual(
            remove_symbols("6439067-89.2023.4.04.5902"), "64390678920234045902"
        )
        self.assertEqual(
            remove_symbols("4976023-82.2012.7.00.2263"), "49760238220127002263"
        )
        self.assertEqual(
            remove_symbols("4976...-02382-.-2012.-7002--263"),
            "49760238220127002263",
        )
        self.assertEqual(
            remove_symbols("4976023-82.2012.7.00.2263*!*&#"),
            "49760238220127002263*!*&#",
        )
        self.assertEqual(
            remove_symbols("4976..#.-0@2382-.#-2012.#-7002--263@"),
            "4976#0@2382#2012#7002263@",
        )
        self.assertEqual(remove_symbols("@...---...#"), "@#")
        self.assertEqual(remove_symbols("...---..."), "")

    def test_generate_processo_juridico(self):
        self.assertEqual(
            generate_processo_juridico()[9:13], str(datetime.now().year)
        )
        self.assertEqual(generate_processo_juridico(ano=3000)[9:13], "3000")
        self.assertEqual(generate_processo_juridico(orgao=4)[13:14], "4")
        self.assertEqual(
            generate_processo_juridico(ano=3000, orgao=4)[9:13], "3000"
        )
        self.assertEqual(generate_processo_juridico(ano=1000, orgao=4), "")
        self.assertFalse(generate_processo_juridico(orgao=0))

    def test_check_sum(self):
        self.assertEqual(_checksum(546611720238150014), "77")
        self.assertEqual(_checksum(403818720238230498), "50")

    def test_is_valid_processo_juridico(self):
        self.assertTrue(is_valid_processo_juridico("10188748220234018200"))
        self.assertTrue(is_valid_processo_juridico("45532346920234025107"))
        self.assertFalse(is_valid_processo_juridico("10188748220239918200"))
        self.assertFalse(is_valid_processo_juridico("00000000000000000000"))
        self.assertFalse(is_valid_processo_juridico("455323469202340251"))
        self.assertFalse(
            is_valid_processo_juridico("455323469202340257123123123")
        )
        self.assertFalse(
            is_valid_processo_juridico("455323423QQWEQWSsasd&*(()")
        )


if __name__ == "__main__":
    unittest.main()
