import exceptions.player_exceptions as pe


class Player:
    __name = ''

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name == "":
            raise pe.EmptyNameError
        if not isinstance(name, str):
            raise pe.NameNotStringError
        self.__name = name

    def is_name_empty(self):
        if self.__name == "":
            return True
        return False
