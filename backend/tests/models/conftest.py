import pytest
from bamboo.database import db


@pytest.fixture(autouse=True)
def init_db():
    db.create_all()
    try:
        yield
    finally:
        db.drop_all()
