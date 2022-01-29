from Jogador import Jogador
from Monstro import Monstro, MonstroSpy
from Ataque import Ataque, AtaqueSpy
import unittest

class Jogo:
    def __init__(self, monstro, jogador):
        self.monstro = monstro
        self.vitoria = False
        self.jogador = jogador

    def __del__(self):
        del self.monstro
        self.vitoria = False

    def atacar(self, ataque):
        if self.monstro.defesa == []:
            self.monstro.gerarDefesa()
           
        self.vitoria = ataque.conferirAtaque(self.monstro.defesa)

        if not self.vitoria:
            self.jogador.vidasDoJogador -= 1

class JogoTests(unittest.TestCase):
    def setUp(self):
        self.jogador = Jogador(5)
        self.monstro = MonstroSpy()
        self.vitoria = False
        self.sut = Jogo(self.monstro, self.jogador)

    def tearDown(self):
        del self.jogador
        del self.monstro
        del self.vitoria
        del self.sut


    def teste_givenSemDefesa_whenAtacar_thenGerarDefesa(self):
        armas = [1,2,3,4]
        ataque = Ataque(armas)
        self.monstro.defesa = []

        self.sut.atacar(ataque)

        self.assertTrue(self.monstro.chamouGerarDefesa)

    def teste_givenComDefesa_whenAtacar_thenNaoGerarDefesa(self):
        armas = [1,2,3,4]
        ataque = Ataque(armas)
        self.monstro.defesa = [1,2,3,4]

        self.sut.atacar(ataque)

        self.assertFalse(self.monstro.chamouGerarDefesa)

    def teste_given2ArmasCertasPosicoesErradas2ArmasCertasPosicoesCertas_whenAcertou2(self):
        armas = [1,2,3,4]
        ataque = AtaqueSpy(armas)
        self.monstro.defesa = [1,3,2,4]

        self.sut.atacar(ataque)

        self.assertEqual(ataque.chamouAcertouAtaque, 2)
        self.assertEqual(ataque.armasCorretasNaPosicaoCorreta, 2)
        self.assertEqual(ataque.armasCorretasNaPosicaoErrada, 2)



if __name__ == '__main__':
    unittest.main(verbosity=2)