import mongoengine
from data.split import Split

class Box(mongoengine.Document):
	leader_user_id = mongoengine.ObjectIdField(required = true)
	name = mongoengine.StringField(required = true)
	description = mongoengine.StringField(required = true)
	state = mongoengine.IntField(default = 0)
	creation_date = mongoengine.DateTimeField(default = datetime.datetime.now)
	splits = mongoengine.EmbeddedDocumentListField(Split)

		meta = {
		'db_alias' = 'core'
		'collection': = 'boxes'
	}
