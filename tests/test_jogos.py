import unittest
from unittest.mock import patch
import velha
import jogos
import forca

class JogosTests(unittest.TestCase):
    def test_vitoria_diagonal(self):
        self.assertEqual(velha.vencedor([[1,-1,0],[0,1,-1],[0,0,1]]),1)
    def test_empate(self):
        self.assertEqual(velha.vencedor([[1,-1,1],[1,-1,-1],[-1,1,1]]),0)
    def test_menu_recupera_opcao_invalida(self):
        with patch('builtins.input',side_effect=['x','0']),patch('builtins.print'):
            jogos.escolhe_jogo()
    def test_forca_revela_todas_as_ocorrencias(self):
        letras=forca.inicializa_letras_acertadas('ARARA')
        forca.marca_chute_correto('A',letras,'ARARA')
        self.assertEqual(letras,['A','_','A','_','A'])
    def test_partida_termina_em_empate(self):
        entradas=['1','1','1','2','1','3','2','2','2','1','2','3','3','2','3','1','3','3']
        with patch('builtins.input',side_effect=entradas),patch('builtins.print') as out:
            velha.jogar()
            out.assert_any_call('Empate!')

if __name__=='__main__':unittest.main()
