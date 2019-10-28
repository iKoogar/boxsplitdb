import bson
import datetime

from data.box import Box
from data.split import Split
from data.user import User

# user stuff ==========================================================================================================

def create_account(name: str, email: str) -> User:
	user = User()
	user.name = name
	user.email = email

	user.save()
	return user


def find_account_by_email(email: str) -> User:
    user = User.objects(email=email).first()
    return user

# box, split stuff ====================================================================================================

def create_box(leader_id: str, name: str, description: str) -> Box:


def set_box_state(state: int):


def add_split_to_box(split: Split):


def get_box_from_id(id: str) -> Box:


def assign_participant_to_split(split: Split, participant_id: str):


def remove_participant_from_split(split: Split, participant_id: str):


