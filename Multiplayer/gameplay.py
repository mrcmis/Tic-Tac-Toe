from board import Board
from player import Player
import time

class Gameplay:
    __board = Board()
    __win_limit = 3
    __player_one = Player()
    __player_two = Player()
    __BUFFER_SIZE = 1000

    def __init__(self, socket_one, socket_two, board_width=3, board_height=3, win_limit=3):
        self.__board = Board(board_width, board_height)
        self.__win_limit = win_limit
        for i in range(board_width):
            for j in range(board_height):
                self.__board.set_element(i, j, '-')
        self.__player_one_socket = socket_one
        self.__player_two_socket = socket_two

        socket_one.send("Write your name".encode())
        socket_two.send("Wait".encode())
        socket_two.recv(self.__BUFFER_SIZE)
        while not self.is_player_name_valid(1):
            data = socket_one.recv(self.__BUFFER_SIZE).decode('utf-8')
            print(data)
            socket_one.send(self.set_player_name(data, 1).encode())
            socket_one.recv(self.__BUFFER_SIZE)
        socket_two.send("Write your name".encode())
        while not self.is_player_name_valid(2):
            data = socket_two.recv(self.__BUFFER_SIZE).decode('utf-8')
            print(data)
            socket_two.send(self.set_player_name(data, 2).encode())
            socket_two.recv(self.__BUFFER_SIZE)


    def is_win(self):
        for i in range(self.__board.get_width()):
            for j in range(self.__board.get_height()):
                if (self.__check_down(i, j, self.__board.get_sign(i, j), 0) or
                        self.__check_right(i, j, self.__board.get_sign(i, j), 0) or
                        self.__check_right_down(i, j, self.__board.get_sign(i, j), 0) or
                        self.__check_right_up(i, j, self.__board.get_sign(i, j), 0)):

                        return True
        return False

    def user_move(self, sign, player_socket):
        player_socket.send('Choose a row: '.encode())
        row = int(player_socket.recv(self.__BUFFER_SIZE).decode('utf-8'))
        player_socket.send('Choose a column: '.encode())
        column = int(player_socket.recv(self.__BUFFER_SIZE).decode('utf-8'))
        if self.__is_not_out_of_board_range(row, column):
            self.__board.set_element(row, column, sign)
        else:
            self.user_move(sign, player_socket)

    def set_board(self, board): #for tests only?
        self.__board = board

    def set_win_limit(self, win_limit): #for tests only?
        self.__win_limit = win_limit

    def __check_down(self, row, column, sign, count):
            if sign == '-':
                return False
            if count == self.__win_limit:
                return True
            if self.__is_not_out_of_board_range(row, column) and self.__board.get_sign(row, column) == sign:
                count = count + 1
                return self.__check_down(row + 1, column, sign, count)
            return False

    def __check_right(self, row, column, sign, count):
            if sign == '-':
                return False
            if count == self.__win_limit:
                return True
            if self.__is_not_out_of_board_range(row, column) and self.__board.get_sign(row, column) == sign:
                count = count + 1
                return self.__check_right(row , column + 1, sign, count)
            return False

    def __check_right_up(self, row, column, sign, count):
            if sign == '-':
                return False
            if count == self.__win_limit:
                return True
            if self.__is_not_out_of_board_range(row, column) and self.__board.get_sign(row, column) == sign:
                count = count + 1
                return self.__check_right_up(row - 1, column + 1, sign, count)
            return False

    def __check_right_down(self, row, column, sign, count):
            if sign == '-':
                return False
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

    def start(self):
        while not self.is_win():
            self.__player_one_socket.send(str(self.__board).encode())
            self.__player_one_socket.recv(self.__BUFFER_SIZE)
            self.__player_one_socket.send("{} turn! Your sign is: O".format(self.__player_one.get_name()).encode())
            self.__player_one_socket.recv(self.__BUFFER_SIZE)
            self.user_move('O', self.__player_one_socket)
            self.__player_one_socket.send(str(self.__board).encode())
            self.__player_one_socket.recv(self.__BUFFER_SIZE)
            if self.is_win():
                self.__player_one_socket.send(str(self.__board).encode())
                self.__player_one_socket.recv(self.__BUFFER_SIZE)
                self.__player_two_socket.send(str(self.__board).encode())
                self.__player_two_socket.recv(self.__BUFFER_SIZE)
                break
            self.__player_two_socket.send(str(self.__board).encode())
            self.__player_two_socket.recv(self.__BUFFER_SIZE)
            self.__player_two_socket.send("{} turn! Your sign is: X".format(self.__player_two.get_name()).encode())
            self.__player_two_socket.recv(self.__BUFFER_SIZE)
            self.user_move('X', self.__player_two_socket)
            self.__player_two_socket.send(str(self.__board).encode())
            self.__player_two_socket.recv(self.__BUFFER_SIZE)
        self.__player_one_socket.send(str(self.__board).encode())
        self.__player_one_socket.recv(self.__BUFFER_SIZE)
        self.__player_two_socket.send(str(self.__board).encode())
        self.__player_two_socket.recv(self.__BUFFER_SIZE)

    def set_player_name(self, name, player):
        if player == 1:
            try:
                self.__player_one.set_name(name)
                return 'Name set.'
            except Exception as error:
                return error.message
        else:
            try:
                self.__player_two.set_name(name)
                return 'Name set.'
            except Exception as error:
                return error.message

    def is_player_name_valid(self, player):
        if player == 1:
            if self.__player_one.is_name_empty():
                return False
            else:
                return True
        else:
            if self.__player_two.is_name_empty():
                return False
            else:
                return True

