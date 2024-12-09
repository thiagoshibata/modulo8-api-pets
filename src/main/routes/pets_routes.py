from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pets_lister_composer import pets_lister_composer
from src.main.composer.pets_deleter_composer import pets_deleter_composer

pets_route_bp = Blueprint("pets_routes", __name__)

@pets_route_bp.route("/pets", methods=["GET"])
def list_pets():
    http_request = HttpRequest()
    view = pets_lister_composer()
    response = view.handle(http_request)

    return jsonify(response.body), response.status_code

@pets_route_bp.route("/pets/<name>", methods=["DELETE"])
def delete_pets(name):
    http_request = HttpRequest(param={"name": name})
    view = pets_deleter_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
