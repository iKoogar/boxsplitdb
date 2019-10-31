import mongoengine
from data.box import Box


class User(mongoengine.Document):
	user_id = mongoengine.ObjectIdField()
	name = mongoengine.StringField(required = True)
	email = mongoengine.StringField(required = True)
	own_boxes = mongoengine.ListField(mongoengine.ReferenceField(Box))
	participant_splits = mongoengine.ListField(mongoengine.ReferenceField(Split))

	# social media stuff

	meta = {
		'db_alias': 'core',
		'collection': 'users'
	}
