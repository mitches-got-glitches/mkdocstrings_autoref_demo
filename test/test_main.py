"""Some spot tests for Gandalf.

Just using as a runner, not actual tests.
"""
from gandalf import Gandalf, Gwaihir, Shadowfax


def test_gandalf_deny():
    Gandalf().deny("glug a pepsi")
    pass


def test_gandalf_cant_deny_without_staff():
    Gandalf(weapon="Narya").deny("chuckle")


def test_set_wrong_weapon_error():
    gandalf = Gandalf()
    gandalf.weapon = "my axe"


def test_gandalf_travel():
    gandalf = Gandalf()
    gandalf.mount = Shadowfax()
    gandalf.travel()
    gandalf.mount = Gwaihir()
    gandalf.travel()


def test_set_right_colour():
    gandalf = Gandalf()
    print(gandalf.colour)
    gandalf.set_colour("white")
    print(gandalf.colour)


def test_set_wrong_colour():
    gandalf = Gandalf()
    print(gandalf.colour)
    gandalf.set_colour("baby blue")
