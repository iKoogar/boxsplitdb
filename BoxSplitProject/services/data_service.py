import bson
import datetime

from data.box import Box
from data.split import Split
from data.user import User

# user stuff =========================================================================================================

def create_account(name: str, email: str) -> User:
	user = User()
	user.name = name
	user.email = email

	user.save()
	return user


def find_account_by_email(email: str) -> User:
    user = User.objects(email=email).first()
    return user

# box, split stuff ==========================================================================================================

def box_create():


def box_state_set():


def box_add_split():


def split_assign_participant():


def split_remove_participant():






