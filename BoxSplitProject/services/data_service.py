import bson
import datetime

from data.box import Box
from data.split import Split
from data.users import Users

def create_account (name::str, email: str) -> User:
	user = User()
	user.name = name
	user.email = email

	user.save()
	return user

def find_account_by_email(email: str) -> User:
    user = User.objects(email=email).first()
    return user