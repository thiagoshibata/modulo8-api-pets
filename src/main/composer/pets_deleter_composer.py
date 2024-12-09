from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.controllers.pets_deleter_controller import PetsDeleterController
from src.views.pets_deleter_view import PetsDeleterView

def pets_deleter_composer():
    model = PetsRepository(db_connection_handler)
    controller = PetsDeleterController(model)
    view = PetsDeleterView(controller)

    return view
