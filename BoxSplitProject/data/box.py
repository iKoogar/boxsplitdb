import mongoengine
import datetime
from data.split import Split


class Box(mongoengine.Document):
	leader_user_id = mongoengine.ObjectIdField(required = True)
	name = mongoengine.StringField(required = True)
	description = mongoengine.StringField(required = True)
	state = mongoengine.IntField(default = 0)
	creation_date = mongoengine.DateTimeField(default = datetime.datetime.now)
	splits = mongoengine.EmbeddedDocumentListField(Split)

	meta = {
		'db_alias' = 'core'
		'collection': = 'boxes'
	}
