import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fastapi_Dunossauro.app import app
from Praticas_sala.ApiBlog.modelos import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        # transforma a fixture em gerador
        yield session

    table_registry.metadata.drop_all(engine)
