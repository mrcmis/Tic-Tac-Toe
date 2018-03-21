from board import Board


class Gameplay:
    __board = Board(4, 4)
    __win_limit = 4

    def __init__(self):
        self.__board.set_element(0, 0, 'a')
        self.__board.set_element(0, 1, 'b')
        self.__board.set_element(0, 2, 'c')
        self.__board.set_element(0, 3, 'd')
        self.__board.set_element(1, 0, 'e')
        self.__board.set_element(1, 1, 'a')
        self.__board.set_element(1, 2, 'g')
        self.__board.set_element(1, 3, 'h')
        self.__board.set_element(2, 0, 'i')
        self.__board.set_element(2, 1, 'j')
        self.__board.set_element(2, 2, 'a')
        self.__board.set_element(2, 3, 'l')
        self.__board.set_element(3, 0, 'q')
        self.__board.set_element(3, 1, 'w')
        self.__board.set_element(3, 2, 'e')
        self.__board.set_element(3, 3, 'p')
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
