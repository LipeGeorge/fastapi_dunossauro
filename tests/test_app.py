from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_dunossauro.app import app

# teste composto de 3 etapas.
# Organizar (arrange), Agir(Act), Afirmar(assert),
# teardown(Desorganizar para o próximo test)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    # Assert (Garanta essa linha para mim)
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olar Mundo!'}  # assert
