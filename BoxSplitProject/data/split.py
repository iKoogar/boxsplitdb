import mongoengine
from data.user import User


class Split(mongoengine.EmbeddedDocument):
    participant = mongoengine.ReferenceField(User)
    name = mongoengine.StringField(required = True)
    description = mongoengine.StringField(required = True)
    state = mongoengine.IntField(default = 0)
    price_cents = mongoengine.IntField(required = True)