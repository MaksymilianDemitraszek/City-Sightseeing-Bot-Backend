from mongoengine import *
import datetime

connect('chatboot')

class Object(Document):
    name = StringField()
    tags = ListField()
    latitude = FloatField()
    longitude = FloatField()




# class Event(Document):
#
#

class History(Document):
    tags = ListField()
    timestamp = DateTimeField(default=datetime.datetime.now())

    def create(self, visited_object):
        self.tags = visited_object.tags
        self.save()
        return self

class CallQueue(Document):
    text = StringField()
    original_lang = StringField()
    is_done = BooleanField(default=False)

