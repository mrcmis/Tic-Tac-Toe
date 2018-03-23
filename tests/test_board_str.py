from unittest import TestCase
import board


class TestBoard(TestCase):
    def test_check_if_str_return_proper_repr(self):
        test_board = board.Board(3, 3)
        test_board.set_element(1, 1, 'x')
        expected_str = "- - - \n\n- x - \n\n- - - \n\n"
        self.assertEqual(test_board.__str__(), expected_str)

    def test_check_if_str_return_proper_repr2(self):
        test_board = board.Board(1, 1)
        test_board.set_element(0, 0, 'x')
        expected_str = "x \n\n"
        self.assertEqual(test_board.__str__(), expected_str)

    def test_check_if_str_return_proper_repr3(self):
        test_board = board.Board(5, 5)
        test_board.set_element(0, 0, 'o')
        test_board.set_element(0, 1, 'x')
        test_board.set_element(0, 2, 'o')
        test_board.set_element(0, 3, 'x')
        test_board.set_element(0, 4, 'o')
        test_board.set_element(1, 4, 'x')
        test_board.set_element(2, 4, 'x')
        test_board.set_element(3, 4, 'o')
        test_board.set_element(4, 4, 'o')
        expected_str = "o x o x o \n\n- - - - x \n\n- - - - x \n\n- - - - o \n\n- - - - o \n\n"
        self.assertEqual(test_board.__str__(), expected_str)

    def test_check_if_str_return_proper_repr4(self):
        test_board = board.Board(2, 3)
        test_board.set_element(0, 0, 'x')
        expected_str = "x - \n\n- - \n\n- - \n\n"
        self.assertEqual(test_board.__str__(), expected_str)

    def test_check_if_str_return_proper_repr4(self):
        test_board = board.Board(2, 2)
        test_board.set_element(0, 0, 'o')
        test_board.set_element(0, 1, 'o')
        test_board.set_element(1, 0, 'o')
        test_board.set_element(1, 1, 'o')
        expected_str = "o o \n\no o \n\n"
        self.assertEqual(test_board.__str__(), expected_str)

    def test_check_if_str_return_proper_repr5(self):
        test_board = board.Board(3, 3)
        expected_str = "- - - \n\n- - - \n\n- - - \n\n"
        self.assertEqual(test_board.__str__(), expected_str)