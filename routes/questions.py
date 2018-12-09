from flask_restful import Resource, reqparse

from models.objects import Object, History

from utils import NearbyObjects

loc_parser = reqparse.RequestParser()
loc_parser.add_argument('problem', required=True)
'''
    Possible options:
    -fine
    -paying tax
    -doctor register
'''

class Question(Resource):
    def get(self):
        args = loc_parser.parse_args()
        if args['problem'] == 'fine':
            return {"solution": ""}

        # if args['problem'] == 'tax':

        if args['problem'] ==  'doctor':
            return {"solution": ""}



