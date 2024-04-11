""" Testing """
import unittest
from unittest.mock import patch
import pyfiglet
from main import generate_random_number, validate_user_inputs, play_again


class TestGame(unittest.TestCase):
    """Tests unitarios"""
    def test_generate_random_number(self):
        """..."""
        number = generate_random_number()
        self.assertTrue(1<=number<=100)

    def test_validate_inputs(self):
        """..."""
        message_low = validate_user_inputs(47, 20)
        self.assertEqual(message_low, pyfiglet.figlet_format("Demasiado bajo:(", font="digital"))

        message_high = validate_user_inputs(30,90)
        self.assertEqual(message_high, pyfiglet.figlet_format("Demasiado alto:(", font="digital"))

        message_winner = validate_user_inputs(20,20)
        self.assertEqual(message_winner, pyfiglet.figlet_format("¡Felicidades!:) ¡Adivinaste el número!", font="digital"))


    def test_play_again_calls_game(self):
        """..."""
        with patch('main.game') as mock_game:
            # Simular la entrada del usuario como "y" para jugar nuevamente
            with patch('builtins.input', return_value='y'):
                play_again()
                # Verificar si la función game fue llamada una vez
                mock_game.assert_called_once()


if __name__ == '__main__':
    unittest.main()
