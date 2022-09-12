import calculadora
import unittest

class Test(unittest.TestCase):

    def test_Suma(self):
        sumacomp =calculadora.Suma((5, 6), (25, 9))
        self.assertAlmostEqual(sumacomp[0], 30)
        self.assertAlmostEqual(sumacomp[1], 15)

    def test_Resta(self):
        restacomp =calculadora.Resta((12, 15), (5, 6))
        self.assertAlmostEqual(restacomp[0], 7)
        self.assertAlmostEqual(restacomp[1], 9)

    def test_Producto(self):
        Produccomp =calculadora.Producto((36, 25), (13, 1))
        self.assertAlmostEqual(Produccomp[0], 443)
        self.assertAlmostEqual(Produccomp[1], 361)

    def test_Division(self):
        Divisioncomp=calculadora.Division((9, 3), (-7, 6))
        self.assertAlmostEqual(Divisioncomp[0], -0.5294117647058824)
        self.assertAlmostEqual(Divisioncomp[1], -0.8823529411764706)

    def test_Modulo(self):
        Modulocomp = calculadora.Modulo((3, 4))
        self.assertAlmostEqual(Modulocomp, 5.0)

    def test_Conjugado(self):
        Conjugadocomp = calculadora.Conjugado((9, 5))
        self.assertAlmostEqual(Conjugadocomp[0], 9)
        self.assertAlmostEqual(Conjugadocomp[1], -5)

    def test_ConversionPolarACartesiano(self):
        ConverPACcomp = calculadora.ConversionPolarACartesiana(4, 6)
        self.assertAlmostEqual(ConverPACcomp[0], 3.978087581473093)
        self.assertAlmostEqual(ConverPACcomp[1], 0.4181138530706139)

    def test_ConversionCartesianoAPolar(self):
        ConverCAPcomp = calculadora.ConversionCartesianaAPolar(3, 4)
        self.assertAlmostEqual(ConverCAPcomp[0], 5.0)
        self.assertAlmostEqual(ConverCAPcomp[1], 53.13010235415598)

    def test_Fase(self):
        fasecomp = calculadora.Fase((16, 2))
        self.assertAlmostEqual(fasecomp, 7.125016348901798)





if __name__ == '__main__':
    unittest.main()