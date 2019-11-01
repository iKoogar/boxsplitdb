import mongoengine



class Split(mongoengine.EmbeddedDocument):
    from data.user import User
    participant = mongoengine.ReferenceField(User)
    name = mongoengine.StringField(required = True)
    description = mongoengine.StringField(required = True)
    state = mongoengine.IntField(default = 0)
    price_cents = mongoengine.IntField(required = True)