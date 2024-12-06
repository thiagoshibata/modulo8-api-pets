from typing import Dict
from abc import ABC, abstractmethod

class PetsListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass
