import mongoengine
import datetime
from data.split import Split


class Box(mongoengine.Document):
	box_id = mongoengine.ObjectIdField()
	leader = ReferenceField(User, required = True)
	name = mongoengine.StringField(required = True)
	description = mongoengine.StringField(required = True)
	state = mongoengine.IntField(default = 0)
	creation_date = mongoengine.DateTimeField(default = datetime.datetime.now)
	splits = mongoengine.EmbeddedDocumentListField(Split)

	meta = {
		'db_alias': 'core',
		'collection': 'boxes'
	}

