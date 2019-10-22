import bson
import datetime


from BoxSplitProject.data.box import Box
from BoxSplitProject.data.split import Split
from BoxSplitProject.data.user import User

def create_account(name: str, email: str) -> User:
	user = User()
	user.name = name
	user.email = email

	user.save()
	return user

def find_account_by_email(email: str) -> User:
    user = User.objects(email=email).first()
    return user