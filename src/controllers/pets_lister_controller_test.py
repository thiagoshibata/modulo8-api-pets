from src.models.sqlite.entities.pets import PetsTable
from .pets_lister_controller import PetsListerController

class MockPetsRespository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="Cat", id=4),
            PetsTable(name="Buddy", type="Dog", id=47)
        ]

def test_list_pets():
    controller = PetsListerController(MockPetsRespository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Fluffy", "id": 4},
                {"name": "Buddy", "id": 47}
            ]
        }
    }

    assert response == expected_response
