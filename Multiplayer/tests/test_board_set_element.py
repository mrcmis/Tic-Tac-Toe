from unittest import TestCase
import board


class TestBoard(TestCase):
    def test_if_set_value(self):
        test_board = board.Board()
        value_to_set = 'x'
        test_board.set_element(0, 0, value_to_set)
        self.assertEqual(test_board.get_board_matrix()[0][0], value_to_set)

    def test_if_set_value2(self):
        test_board = board.Board(5, 5)
        value_to_set = 'x'
        test_board.set_element(4, 4, value_to_set)
        self.assertEqual(test_board.get_board_matrix()[4][4], value_to_set)

    def test_if_set_value3(self):
        test_board = board.Board(2, 2)
        value_to_set = 'x'
        test_board.set_element(0, 0, value_to_set)
        self.assertEqual(test_board.get_board_matrix()[0][0], value_to_set)

    def test_if_does_not_set_value_in_improper_range(self):
        test_board = board.Board(5, 5)
        copy = test_board.get_board_matrix()
        value_to_set = 'x'
        test_board.set_element(8, 9, value_to_set)
        self.assertEqual(test_board.get_board_matrix(), copy)

    def test_if_does_not_set_value_in_improper_range2(self):
        test_board = board.Board(1, 1)
        copy = test_board.get_board_matrix()
        value_to_set = 'o'
        test_board.set_element(12222, 334452, value_to_set)
        self.assertEqual(test_board.get_board_matrix(), copy)