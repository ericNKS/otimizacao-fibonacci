import unittest

from comparacao import comparar


class ComparacaoTest(unittest.TestCase):
    def test_compara_resultados_e_tempos(self):
        resultados = comparar([0, 8, 12], repeticoes=3)
        self.assertEqual([r['resultado'] for r in resultados], [0, 21, 144])
        for linha in resultados:
            self.assertGreater(linha['recursivo_s'], 0)
            self.assertGreater(linha['iterativo_s'], 0)
            self.assertGreater(linha['aceleracao'], 0)


if __name__ == '__main__':
    unittest.main()
