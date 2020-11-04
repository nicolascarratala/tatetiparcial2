class TaTeTi():
    def __init__(self):
        self.tablero_inicial = '1.1|1.2|1.3\n---+---+---\n2.1|2.2|2.3\n---+---+---\n3.1|3.2|3.3'
        self.positions = ['1.1', '1.2', '1.3',
                          '2.1', '2.2', '2.3',
                          '3.1', '3.2', '3.3']
        self.board = {value: value for value in self.positions}
        self.valid = ['1.1', '1.2', '1.3',
                      '2.1', '2.2', '2.3',
                      '3.1', '3.2', '3.3']

    def game(self):
        self.piece = 'x'

        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'

        if len(self.valid) == 0:
            winner = 'Ninguno'

        return winner

    def win(self):

        jugador = ' x '

        jugadores = [' x ', ' o ']

        result = False

        for jugador in jugadores:

            # diagonal a
            if self.board['1.1'] == jugador and self.board['2.2'] == jugador and self.board['3.3'] == jugador:
                result = True

            # diagonal b
            if self.board['1.3'] == jugador and self.board['2.2'] == jugador and self.board['3.1'] == jugador:
                result = True

            # vertical a
            if self.board['1.1'] == jugador and self.board['2.1'] == jugador and self.board['3.1'] == jugador:
                result = True

            # vertical b
            if self.board['1.2'] == jugador and self.board['2.2'] == jugador and self.board['3.2'] == jugador:
                result = True

            # vertical c
            if self.board['1.3'] == jugador and self.board['2.3'] == jugador and self.board['3.3'] == jugador:
                result = True

            # horizontal a
            if self.board['1.1'] == jugador and self.board['1.2'] == jugador and self.board['1.3'] == jugador:
                result = True

            # horizontal b
            if self.board['2.1'] == jugador and self.board['2.2'] == jugador and self.board['2.3'] == jugador:
                result = True

            # horizontal c
            if self.board['3.1'] == jugador and self.board['3.2'] == jugador and self.board['3.3'] == jugador:
                result = True


        return result









    def input_position(self):
        while(True):
            self.eleccion = str(input('escriba una posición'))
            for valido in self.valid:
                if valido == self.eleccion:
                    self.valid.remove(valido)
                    return self.eleccion


    def __str__(self):
        self.expected = self.tablero_inicial
        return self.expected


if __name__ == '__main__':
    game = TaTeTi()
    print('Ganó ' + game.game())
