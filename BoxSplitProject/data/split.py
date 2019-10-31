import mongoengine
from data.user import User
form data.box import Box


class Split(mongoengine.EmbeddedDocument):
    parent_box = mongoengine.ReferenceField(Box, required = True)
    participant = mongoengine.ReferenceField(User)
    name = mongoengine.StringField(required = True)
    description = mongoengine.StringField(required = True)
    state = mongoengine.IntField(default = 0)
    price_cents = mongoengine.IntField(required = True)