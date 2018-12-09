from flask_restful import Resource, reqparse

from models.objects import Object, History, CallQueue

from utils.call import make_call
from utils.translate import translate_text_to_eng, detect_lang

text_parser = reqparse.RequestParser()
text_parser.add_argument('text', required=True)

class Call(Resource):
    def post(self):
        args = text_parser.parse_args()
        call = CallQueue()
        call.original_lang = detect_lang(args['text'])
        call.text = translate_text_to_eng(args['text'])
        call.save()
        make_call()
        return 200

