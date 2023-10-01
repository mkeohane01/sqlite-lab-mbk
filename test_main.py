"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load


def test_extract_and_load():
    extract()
    db = load()
    assert db is not None
    
