import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'seguranca-informacao/verificador-senhas'))
from gerador_senhas import GeradorSenhas

class GeneratorTests(unittest.TestCase):
    def test_lengths_and_character_groups(self):
        generator = GeradorSenhas()
        for length in [4, 12, 32]:
            password = generator.gerar_senha(length)
            self.assertEqual(len(password), length)
            for group in [generator.letras_minusculas, generator.letras_maiusculas, generator.numeros, generator.especiais]:
                self.assertTrue(any(c in group for c in password))

    def test_no_noncryptographic_randomness(self):
        with patch('random.sample', side_effect=AssertionError), patch('random.choice', side_effect=AssertionError), patch('random.shuffle', side_effect=AssertionError), patch('random.randint', side_effect=AssertionError):
            generator = GeradorSenhas()
            generator.gerar_senha()
            generator.gerar_senha_memoravel()
            self.assertEqual(len(generator.gerar_passphrase().split('-')), 4)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            GeradorSenhas().gerar_senha(3)
