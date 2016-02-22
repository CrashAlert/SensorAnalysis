from flask_restful import Resource, request, reqparse

from backend.database_handler import store_session

parser = reqparse.RequestParser()

class CSVApi(Resource):
    """
    Api to store csvs (post)
    """

    def post(self, session):
        # TODO: assure security
        store_session(session, request.form['body'])
