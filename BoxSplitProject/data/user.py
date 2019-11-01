import mongoengine
from data.box import Box
from data.split import Split


class User(mongoengine.Document):
	user_id = mongoengine.ObjectIdField()
	name = mongoengine.StringField(required = True)
	email = mongoengine.StringField(required = True)
	own_boxes = mongoengine.ListField(mongoengine.ReferenceField(Box))
	own_splits = mongoengine.EmbeddedDocumentListField(Split)

	# social media stuff

	meta = {
		'db_alias': 'core',
		'collection': 'users'
	}
