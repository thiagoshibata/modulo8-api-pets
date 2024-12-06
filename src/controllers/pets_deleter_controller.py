from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.controllers.interfaces.pets_deleter_controller import PetsDeleterControllerInterface

class PetsDeleterController(PetsDeleterControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def delete(self, name: str) -> None:
        self.__pets_repository.delete_pets(name)
