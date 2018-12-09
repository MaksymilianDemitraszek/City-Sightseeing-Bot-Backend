from flask_restful import Resource, reqparse

from models.objects import Object, History

finder_parser = reqparse.RequestParser()
finder_parser.add_argument('object', required=True)

object_parser = reqparse.RequestParser()
object_parser.add_argument('name', required=True)
object_parser.add_argument('tags', required=True)
object_parser.add_argument('lat', required=True)
object_parser.add_argument('long', required=True)

class Find(Resource):
    def get(self):
        args = finder_parser.parse_args()
        keywords = args['object'].split(' ')
        print()
        obj = []
        for key in keywords:
            obj += Object.objects(__raw__={'tags': key})
        if obj == []: return 404
        History().create(obj[0])
        return {'name': obj[0].name,
                'lat': obj[0].latitude,
                'long': obj[0].longitude,
                }, 200

    # def post(self):
    #     args = object_parser.parse_args()
    #     obj = Object()
    #     obj.name = args['name']
    #     obj.tags = tuple(args['tags'])
    #     obj.latitude = float(args['lat'])
    #     obj.longitude = float(args['long'])
    #     obj.save()
    #     return 200




