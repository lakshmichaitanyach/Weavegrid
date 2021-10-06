from .browse import RootAPI, BrowseAPI, CreateFolder, CreateFile
from flask_restful import Resource, reqparse


def initialize_routes(api):
    '''
    function to route api
    '''
    api.add_resource(RootAPI, '/')
    api.add_resource(BrowseAPI, '/<path:req_path>')
    api.add_resource(CreateFolder, '/create-folder/<path:req_path>', defaults={'req_path': None})
    api.add_resource(CreateFile, '/create-file/<path:req_path>', defaults={'req_path': None})


    






