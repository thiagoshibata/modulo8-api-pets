from abc import ABC, abstractmethod

class PetsDeleterControllerInterface(ABC):

    @abstractmethod
    def delete(self, name: str) -> None:
        pass
