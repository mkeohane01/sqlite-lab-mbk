"""
Test goes here

"""

from crud import CRUD


def test_db_create():
    crud = CRUD()
    db = crud.create()
    assert db is not None
    
