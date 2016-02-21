from flask_restful import Resource, request, reqparse


parser = reqparse.RequestParser()

class CSVApi(Resource):
    """
    Api to store csvs (post)
    """

    def post(self, session):
        print(session)
        return