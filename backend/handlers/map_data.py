from flask_restful import Resource, request, reqparse


parser = reqparse.RequestParser()

class MapApi(Resource):
    """
    Api to convert sensor sessions to displayable json data
    """

    def get(self, file_name):
        print(file_name)
        return