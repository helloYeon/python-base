"""class002_inheritance"""

import abc
from typing import Any


class Smartphone(metaclass=abc.ABCMeta):
    """Smartphone Class"""

    def __init__(self, brand, price) -> None:
        self._brand = brand
        self._price = price

    def __str__(self) -> str:
        return f"str : {self._brand} - {self._price}"

    @abc.abstractmethod
    def func1(self) -> int:
        """_summary_"""
        pass

    @property
    def price(self) -> Any:
        """Smartphone Class"""
        return self._price

    @price.setter
    def price(self, price) -> None:
        if price < 0:
            raise ValueError("Price below 0 is not possible")
        self._price = price


class Galaxy(Smartphone):
    """_summary_"""

    test_dict = {"a": 1, "b": 2}

    def __init__(self, price, country) -> None:
        super().__init__("Galaxy", price)
        self._country = country

    def __str__(self) -> str:
        return (
            f"str : {self._brand} - {self._price} - {self._country} - {self.__class__} "
        )

    def func1(self) -> dict:
        """_summary_"""
        return self.test_dict
        pass


class Iphone(Smartphone):
    """_summary_"""

    def __init__(self, price, country) -> None:
        super().__init__("IPhone", price)
        self._country = country

    def __str__(self) -> str:
        return (
            f"str : {self._brand} - {self._price} - {self._country} - {self.__class__} "
        )

    def func1(self) -> str:
        """_summary_"""
        return "func1"


# iphone
iphone = Iphone(5000, "america")
# print(iphone)

# galaxy
galaxy = Galaxy(7000, "korea")
# print(galaxy)
