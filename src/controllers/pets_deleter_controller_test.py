from .pets_deleter_controller import PetsDeleterController

def test_delete_pet(mocker):
    mock_repository = mocker.Mock()
    controller = PetsDeleterController(mock_repository)
    controller.delete("amiguinho")

    mock_repository.delete_pets.assert_called_once_with("amiguinho")
