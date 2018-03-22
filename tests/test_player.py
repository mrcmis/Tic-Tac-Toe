from unittest import TestCase
import player
import exceptions.player_exceptions as pe


class TestPlayer(TestCase):
    def test_set_empty_string(self):
        test_player = player.Player()
        try:
            test_player.set_name("")
        except Exception as error:
            print(error.message)
        self.assertRaises(pe.EmptyNameError)

    def test_set_not_string(self):
        test_player = player.Player()
        try:
            test_player.set_name(1)
        except Exception as error:
            print(error.message)
        self.assertRaises(pe.NameNotStringError)
