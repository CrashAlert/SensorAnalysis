from backend.handlers.map_data import MapApi
from backend.handlers.store_data import CSVApi


def add_routes(api):
    api.add_resource(MapApi, '/map/<string:file_name>')
    api.add_resource(CSVApi, '/store/<string:session>')
