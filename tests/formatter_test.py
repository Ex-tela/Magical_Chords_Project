import pytest
from magical_chords import chord_formatter


def test_answer():
    assert chord_formatter.format('abc') == '<p>&nbsp;&nbsp;&nbsp;</p> <p>abc</p>'


if __name__ == "__main__":
    pytest.main(["-s", "-v", __file__])
