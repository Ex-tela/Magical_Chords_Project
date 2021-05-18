import pytest
from magical_chords import chord_formatter

def test_answer():
    assert chord_formatter.format('abc') == 'abc'