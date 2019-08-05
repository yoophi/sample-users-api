from flask import Blueprint
from flask_restful import Api, Resource

main = Blueprint('main', __name__)


class MainResource(Resource):
    def get(self):
        """
        health check
        ---
        tags:
        - default
        responses:
          200:
            description: "Success"
        """

        return {}


main_api = Api(main)
main_api.add_resource(MainResource, "/", endpoint="index")
