"""Defines the main Gandalf class."""
from typing import Literal, get_args

from .utils import Mount

WEAPONS = Literal["Glamdring", "Narya", "Staff"]
COLOURS = Literal["white", "grey"]


class Gandalf:
    """A Gandalf class.

    Attributes:
        colour: The colour of Gandalf's robes. Defaults to 'grey'.
    """

    colour: str = "grey"

    def __init__(self, weapon: WEAPONS = "Staff"):
        """Initialises Gandalf.

        Attributes:
            weapon: The weapon that Gandalf wields, defaults to 'Staff'.
            mount: Gandalf's current steed, defaults to None.
        """
        self._weapon = weapon
        self._mount = None

    @classmethod
    def set_colour(cls, colour: COLOURS):
        """Set Gandalf's colour."""
        if colour not in get_args(COLOURS):
            raise ImproperGandalfColourError
        cls.colour = colour

    @property
    def weapon(self):
        """The weapon property."""
        return self._weapon

    @weapon.setter
    def weapon(self, weapon: WEAPONS):
        """Setter for the weapon property."""
        if weapon not in get_args(WEAPONS):
            raise WrongWeaponError
        self._weapon = weapon

    @property
    def mount(self):
        """Gandalf's mount."""
        return self._mount

    @mount.setter
    def mount(self, mount: Mount):
        """Setter for the mount property."""
        self._mount = mount

    def deny(self, verb: str) -> None:
        """Shout a denial of a doing word.

        Args:
            verb: An action word to deny someone of.
        """
        if not self.weapon == "Staff":
            raise NeedStaffToDenyError("Gandalf doesn't have weapon set to 'Staff'.")
        print(f"YOU SHALL NOT {verb.upper()}!!!")

    def travel(self) -> None:
        """Ride mount to destination."""
        if not self.mount:
            raise NoMountSetError("Gandalf needs a mount to travel.")
        self.mount.ride()


class NoMountSetError(Exception):
    """Raise when no mount is set for Gandalf.."""


class NeedStaffToDenyError(Exception):
    """Raise when Gandalf tries to deny without his staff."""


class ImproperGandalfColourError(Exception):
    """Raise when user tries to set Gandalf to the wrong colour."""


class WrongWeaponError(Exception):
    """Raise when user tries to set a wrong weapon for Gandalf."""

    def __str__(self):
        return f"Chosen weapon must be one of {get_args(WEAPONS)}"


if __name__ == "__main__":
    gandalf = Gandalf()
    gandalf.deny("glamp")
    gandalf.weapon = "Glamdring"
    gandalf.deny("pass")
