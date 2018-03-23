class Board:
    __width = 0
    __height = 0
    __matrix_board = []

    def __init__(self, width=3, height=3):
        self.__width = width
        self.__height = height
        self.__matrix_board = [["-" for _ in range(width)] for _ in range(height)]

    def __str__(self):
        return self._to_string()

    def set_element(self, row, column, value):
        if row in range(self.__height) and column in range(self.__width):
            self.__matrix_board[row][column] = value

    def _to_string(self):
        board_repr = ""
        for i in range(self.__height):
            for j in range(self.__width):
                board_repr = board_repr + self.__matrix_board[i][j] + " "
            board_repr = board_repr + "\n\n"
        return board_repr

    def get_board_matrix(self):
        return self.__matrix_board.copy()

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_sign(self, row, column):
        return self.__matrix_board.copy()[row][column]

