"""Some Gandalf utils."""
from abc import ABC, abstractmethod


class Mount(ABC):
    """A mount for Gandalf."""

    @staticmethod
    @abstractmethod
    def ride() -> None:
        """Ride the mount."""


class Shadowfax(Mount):
    """A fast white pony."""

    @staticmethod
    def ride():
        print("WEEEEEE!")


class Gwaihir(Mount):
    """A great big f**king eagle."""

    @staticmethod
    def ride():
        print("Whoooooooooosh")
