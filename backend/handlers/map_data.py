from flask_restful import Resource, request, reqparse

from backend.database_handler import get_session_as_json

parser = reqparse.RequestParser()


class MapApi(Resource):
    """
    Api to convert sensor sessions to displayable json data
    """

    def get(self, file_name):
        return get_session_as_json(file_name)