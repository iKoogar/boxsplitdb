import mongoengine

class User(mongoengine.Document):
	user_id = mongoengine.ObjectIdField(required = true)
	name = mongoengine.StringField(required = true)
	email = mongoengine.StringField(required = true)

	# social media stuff

	meta = {
		'db_alias' = 'core'
		'collection': = 'users'
	}