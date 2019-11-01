import mongoengine
import datetime
from split import Split
from user import User


class Box(mongoengine.Document):
    box_id = mongoengine.ObjectIdField()
    leader = mongoengine.ReferenceField(User, required=True)
    name = mongoengine.StringField(required=True)
    description = mongoengine.StringField(required=True)
    state = mongoengine.IntField(default=0)
    creation_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    splits = mongoengine.EmbeddedDocumentListField(Split)

    meta = {
        'db_alias': 'core',
        'collection': 'boxes'
    }
