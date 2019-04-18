# -*- coding: utf-8 -*-


class Game:

    def __init__(self, name: str, category: str, console: str) -> None:
        self.__name = name
        self.__category = category
        self.__console = console

    @property
    def name(self) -> str:
        return self.__name

    @property
    def category(self) -> str:
        return self.__category

    @property
    def console(self) -> str:
        return self.__console
