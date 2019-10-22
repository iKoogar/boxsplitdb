import mongoengine


class User(mongoengine.Document):
	user_id = mongoengine.ObjectIdField(required = True)
	name = mongoengine.StringField(required = True)
	email = mongoengine.StringField(required = True)

	# social media stuff

	#meta = {
	#	'db_alias' = 'core'
	#	'collection': = 'users'
	#}