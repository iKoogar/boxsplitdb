import mongoengine


class User(mongoengine.Document):
	from data.box import Box
	user_id = mongoengine.ObjectIdField()
	name = mongoengine.StringField(required = True)
	email = mongoengine.StringField(required = True)
	own_boxes = mongoengine.ListField(mongoengine.ReferenceField(Box))

	# social media stuff

	meta = {
		'db_alias': 'core',
		'collection': 'users'
	}
