import mongoengine


class Split(mongoengine.EmbeddedDocument):
	leader_user_id = mongoengine.ObjectIdField(required = True)
	name = mongoengine.StringField(required = True)
	description = mongoengine.StringField(required = True)
	state = mongoengine.IntField(default = 0)
	price_cents = mongoengine.IntField(required = True)