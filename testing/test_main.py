from main import get_none
from main import flatten_dict


def test_get_none():
    assert get_none() is None


def test_flatten_dict():
    assert flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [{'inner_a': 42, 'inner_b': 350}, 3.14]
