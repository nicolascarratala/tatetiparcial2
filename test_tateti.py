import unittest
from unittest.mock import patch
from tateti import TaTeTi
from parameterized import parameterized


class Test(unittest.TestCase):
    def test_tablero_inicial(self):
        game = TaTeTi()
        expected = '1.1|1.2|1.3\n---+---+---\n2.1|2.2|2.3\n'
        expected += '---+---+---\n3.1|3.2|3.3'
        self.assertEqual(game.__str__(), expected)

    def test_tablero_diccionario(self):
        game = TaTeTi()
        positions = ['1.1', '1.2', '1.3',
                     '2.1', '2.2', '2.3',
                     '3.1', '3.2', '3.3']
        board = {value: value for value in positions}
        self.assertEqual(game.board, board)

    def test_input_position_1(self):
        game = TaTeTi()
        valid = ['1.1', '1.2', '1.3',
                 '2.1', '2.3',
                 '3.1', '3.2', '3.3']
        with patch('builtins.input', side_effect=['4.4', '2.2']):
            game.input_position()
            self.assertEqual(game.valid, valid)

    @parameterized.expand(['1.1', '1.2', '1.3',
                           '2.1', '2.2', '2.3',
                           '3.1', '3.2', '3.3'])
    def test_input_position_2(self, position):
        game = TaTeTi()
        with patch('builtins.input', side_effect=['6.1', '7.7', position]):
            self.assertEqual(game.input_position(), position)

    @parameterized.expand([({'1.1': ' x ', '1.2': '1.2', '1.3': ' o ',
                             '2.1': ' o ', '2.2': ' x ', '2.3': '2.3',
                             '3.1': '3.1', '3.2': '3.2', '3.3': ' x '},
                            True),
                           ({'1.1': ' x ', '1.2': '1.2', '1.3': '1.3',
                             '2.1': ' x ', '2.2': '2.2', '2.3': '2.3',
                             '3.1': ' x ', '3.2': '3.2', '3.3': '3.3'},
                            True),
                           ({'1.1': '1.1', '1.2': ' o ', '1.3': '1.3',
                             '2.1': '2.1', '2.2': ' o ', '2.3': '2.3',
                             '3.1': '3.1', '3.2': ' o ', '3.3': '3.3'},
                            True),
                           ({'1.1': '1.1', '1.2': '1.2', '1.3': ' x ',
                             '2.1': '2.1', '2.2': ' x ', '2.3': '2.3',
                             '3.1': ' x ', '3.2': '3.2', '3.3': '3.3'},
                            True),
                           ({'1.1': ' o ', '1.2': ' o ', '1.3': ' o ',
                             '2.1': '2.1', '2.2': '2.2', '2.3': '2.3',
                             '3.1': '3.1', '3.2': '3.2', '3.3': '3.3'},
                            True),
                           ({'1.1': '1.1', '1.2': '1.2', '1.3': '1.3',
                             '2.1': ' x ', '2.2': ' x ', '2.3': ' x ',
                             '3.1': '3.1', '3.2': '3.2', '3.3': '3.3'},
                            True),
                           ({'1.1': '1.1', '1.2': '1.2', '1.3': ' x ',
                             '2.1': '2.1', '2.2': ' o ', '2.3': '2.3',
                             '3.1': ' x ', '3.2': '3.2', '3.3': '3.3'},
                            False),
                           ({'1.1': ' x ', '1.2': ' x ', '1.3': ' o ',
                             '2.1': ' o ', '2.2': ' o ', '2.3': ' x ',
                             '3.1': ' x ', '3.2': ' x ', '3.3': ' o '},
                            False),
                           ({'1.1': ' x ', '1.2': '1.2', '1.3': ' o ',
                             '2.1': ' x ', '2.2': ' o ', '2.3': '2.3',
                             '3.1': '3.1', '3.2': '3.2', '3.3': ' x '},
                            False)])
    def test_win(self, board, result):
        game = TaTeTi()
        game.board = board
        self.assertEqual(game.win(), result)

    def test_game(self):
        game = TaTeTi()
        game.board = {'1.1': ' o ', '1.2': ' o ', '1.3': ' x ',
                      '2.1': ' x ', '2.2': ' x ', '2.3': ' o ',
                      '3.1': ' o ', '3.2': ' x ', '3.3': '3.3'}
        game.valid = ['3.3']
        with patch('builtins.input', side_effect=['1.1', '2.2', '3.3']):
            self.assertEqual(game.game(), 'Ninguno')


if __name__ == '__main__':
    unittest.main()
