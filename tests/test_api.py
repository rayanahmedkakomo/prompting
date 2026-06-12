from ai_toolbox import add


def test_add_ints():
    assert add(1, 2) == 3


def test_add_floats():
    assert add(2.5, 0.5) == 3.0
