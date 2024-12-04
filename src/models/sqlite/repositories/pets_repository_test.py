# testes unitários com Mock
from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[(
                [mock.call.query(PetsTable)], # para essa query
                [ #retorne esse resultado
                    PetsTable(name="dog", type="dog"),
                    PetsTable(name="cat", type="cat")
                ]
            )]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found #efeito segundário

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    #se a query foi chamada uma vez com PetsTable
    mock_connection.session.query.assert_called_once_with(PetsTable)
    #se o metodo all foi chamado uma vez
    mock_connection.session.all.assert_called_once()
    #se nao utilizei a propriedade filter
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"

def test_list_pets_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    #se a query foi chamada uma vez com PetsTable
    mock_connection.session.query.assert_called_once_with(PetsTable)
    #se o metodo all não foi chamado
    mock_connection.session.all.assert_not_called()
    #se nao utilizei a propriedade filter
    mock_connection.session.filter.assert_not_called()

    assert response == []

def test_delete_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    repo.delete_pets("petName")

    #se a query foi chamada uma vez com PetsTable
    mock_connection.session.query.assert_called_once_with(PetsTable)
    # se foi filtrado uma vez com o nome "petName"
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == "petName")
    # se o método delete foi chamado uma vez
    mock_connection.session.delete.assert_called_once()

def test_delete_pets_error():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_pets("petName")

    mock_connection.session.rollback.assert_called_once()
