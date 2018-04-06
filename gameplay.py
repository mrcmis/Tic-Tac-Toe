from board import Board
from player import Player


class Gameplay:
    _board = Board()
    _win_limit = 4
    __player_one = Player()
    __player_two = Player()

    def __init__(self, board_width=3, board_height=3, win_limit=3):
        self._board = Board(board_width, board_height)
        self._win_limit = win_limit
        for i in range(board_width):
            for j in range(board_height):
                self._board.set_element(i, j, '-')
        while self.__player_one.is_name_empty() or self.__player_two.is_name_empty():
            try:
                self.__player_one.set_name(input("Input first player name "))
                self.__player_two.set_name(input("Input second player name "))
            except Exception as error:
                print(error.message)

    def is_win(self):
        for i in range(self._board.get_height()):
            for j in range(self._board.get_width()):
                if (self._check_down(i, j, self._board.get_sign(i, j), 0) or
                        self._check_right(i, j, self._board.get_sign(i, j), 0) or
                        self._check_right_down(i, j, self._board.get_sign(i, j), 0) or
                        self._check_right_up(i, j, self._board.get_sign(i, j), 0)):

                        return True
        return False

    def user_move(self, sign):
        row = int(input('Choose a row: '))
        column = int(input('Choose a column: '))
        if self._is_not_out_of_board_range(row, column) and self._board.get_sign(row, column) == '-':
            self._board.set_element(row, column, sign)
        else:
            self.user_move(sign)

    def set_board(self, board): #for tests only?
        self._board = board

    def set_win_limit(self, win_limit): #for tests only?
        self._win_limit = win_limit

    def _check_down(self, row, column, sign, count):
            if sign == '-':
                return False
            if count == self._win_limit:
                return True
            if self._is_not_out_of_board_range(row, column) and self._board.get_sign(row, column) == sign:
                count = count + 1
                return self._check_down(row + 1, column, sign, count)
            return False

    def _check_right(self, row, column, sign, count):
            if sign == '-':
                return False
            if count == self._win_limit:
                return True
            if self._is_not_out_of_board_range(row, column) and self._board.get_sign(row, column) == sign:
                count = count + 1
                return self._check_right(row, column + 1, sign, count)
            return False

    def _check_right_up(self, row, column, sign, count):
            if sign == '-':
                return False
            if count == self._win_limit:
                return True
            if self._is_not_out_of_board_range(row, column) and self._board.get_sign(row, column) == sign:
                count = count + 1
                return self._check_right_up(row - 1, column + 1, sign, count)
            return False

    def _check_right_down(self, row, column, sign, count):
            if sign == '-':
                return False
            if count == self._win_limit:
                return True
            if self._is_not_out_of_board_range(row, column) and self._board.get_sign(row, column) == sign:
                count = count + 1
                return self._check_right_down(row + 1, column + 1, sign, count)
            return False

    def _is_not_out_of_board_range(self, row, column):
            width_border = range(self._board.get_width())
            height_border = range(self._board.get_height())
            if column in width_border and row in height_border:
                return True
            else:
                return False

    def start(self):
        self._board = Board(int(input("width of board: ")), int(input("height of board: ")))
        self._win_limit = int(input("win limit: "))

        while not self.is_win():
            print("{} turn! Your sign is: O".format(self.__player_one.get_name()))
            self.user_move('O')
            print(self._board)
            if self.is_win():
                break
            print("{} turn! Your sign is: X".format(self.__player_two.get_name()))
            self.user_move('X')
            print(self._board)
