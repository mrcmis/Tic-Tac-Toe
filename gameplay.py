from board import Board


class Gameplay:
    __board = Board()
    __win_limit = 4

    def __init__(self, board_width=3, board_height=3, win_limit=3):
        self.__board = Board(board_width, board_height)
        self.__win_limit = win_limit
        for i in range(board_width):
            for j in range(board_height):
                self.__board.set_element(i, j, '-')
        print(self.__board)

    def is_win(self):
        for i in range(self.__board.get_width()):
            for j in range(self.__board.get_height()):
                if (self.__check_down(i, j, self.__board.get_sign(i, j), 0) or
                        self.__check_right(i, j, self.__board.get_sign(i, j), 0) or
                        self.__check_right_down(i, j, self.__board.get_sign(i, j), 0) or
                        self.__check_right_up(i, j, self.__board.get_sign(i, j), 0)):

                        return True
        return False

    def user_move(self, sign):
        row = int(input('Choose a row: '))
        column = int(input('Choose a column: '))
        if self.__is_not_out_of_board_range(row, column):
            self.__board.set_element(row, column, sign)
        else:
            self.user_move(sign)

    def set_board(self, board): #for tests only?
        self.__board = board

    def set_win_limit(self, win_limit): #for tests only?
        self.__win_limit = win_limit

    def __check_down(self, row, column, sign, count):
            if count == self.__win_limit:
                return True
            if self.__is_not_out_of_board_range(row, column) and self.__board.get_sign(row, column) == sign:
                count = count + 1
                return self.__check_down(row + 1, column, sign, count)
            return False

    def __check_right(self, row, column, sign, count):
            if count == self.__win_limit:
                return True
            if self.__is_not_out_of_board_range(row, column) and self.__board.get_sign(row, column) == sign:
                count = count + 1
                return self.__check_right(row , column + 1, sign, count)
            return False

    def __check_right_up(self, row, column, sign, count):
            if count == self.__win_limit:
                return True
            if self.__is_not_out_of_board_range(row, column) and self.__board.get_sign(row, column) == sign:
                count = count + 1
                return self.__check_right_up(row - 1, column + 1, sign, count)
            return False

    def __check_right_down(self, row, column, sign, count):
            if count == self.__win_limit:
                return True
            if self.__is_not_out_of_board_range(row, column) and self.__board.get_sign(row, column) == sign:
                count = count + 1
                return self.__check_right_down(row + 1, column + 1, sign, count)
            return False

    def __is_not_out_of_board_range(self, row, column):
            width_border = range(self.__board.get_width())
            height_border = range(self.__board.get_height())
            if column in width_border and row in height_border:
                return True
            else:
                return False
