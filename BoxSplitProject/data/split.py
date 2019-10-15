import mongoengine

class Split(mongoengine.EmbeddedDocument):
	leader_user_id = mongoengine.ObjectIdField(required = true)
	name = mongoengine.StringField(required = true)
	description = mongoengine.StringField(required = true)
	state = mongoengine.IntField(default = 0)
	price_cents = mongoengine.IntField(required = true)

	meta = {
		'db_alias' = 'core'
		'collection': = 'splits'
	}